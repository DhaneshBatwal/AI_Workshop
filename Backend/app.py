import os
import uuid

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from postgrest import APIError
from supabase import Client, create_client

load_dotenv()

app = Flask(__name__)

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_PUBLISHABLE_KEY")
if not supabase_url or not supabase_key:
    raise RuntimeError("SUPABASE_URL and SUPABASE_PUBLISHABLE_KEY must be set")
supabase: Client = create_client(supabase_url, supabase_key)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        return "", 204


def error_response(message, status):
    return jsonify({"error": message}), status


def valid_uuid(value):
    try:
        return str(uuid.UUID(str(value)))
    except (ValueError, TypeError, AttributeError):
        return None


def supabase_error_response(error):
    # Avoid returning database internals to API callers.
    return error_response("Database request failed", 500)


def event_with_seat_counts(event):
    event = dict(event)
    registration_count = supabase.table("registrations").select(
        "id", count="exact", head=True
    ).eq("event_id", event["id"]).execute().count or 0
    capacity = event.get("capacity")
    event["registration_count"] = registration_count
    event["available_seats"] = max(int(capacity) - registration_count, 0) if capacity is not None else None
    event["is_full"] = capacity is not None and registration_count >= int(capacity)
    return event


@app.get("/")
def index():
    return jsonify({"message": "Events API", "endpoints": [
        "GET /api/users",
        "GET /api/events",
        "POST /api/events",
        "GET /api/events/<event_id>",
        "POST /api/registrations",
        "GET /api/me/registrations?user_id=<user_id>",
        "GET /api/events/<event_id>/registrations",
    ]})


@app.get("/api/users")
def list_users():
    try:
        response = supabase.table("users").select("id, email, role").order("email").execute()
        return jsonify(response.data), 200
    except APIError as error:
        return supabase_error_response(error)


@app.post("/api/events")
def create_event():
    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        return error_response("Request body must be a JSON object", 400)

    organizer_id = valid_uuid(body.get("organizer_id"))
    title = body.get("title")
    if not organizer_id:
        return error_response("organizer_id must be a valid UUID", 400)
    if not isinstance(title, str) or not title.strip():
        return error_response("title is required", 400)

    capacity = body.get("capacity")
    if capacity is not None:
        try:
            capacity = int(capacity)
        except (TypeError, ValueError):
            return error_response("capacity must be a positive integer", 400)
        if capacity < 1 or capacity > 32767:
            return error_response("capacity must be between 1 and 32767", 400)

    payload = {
        "organizer_id": organizer_id,
        "title": title.strip(),
        "capacity": capacity,
        "status": str(body.get("status") or "open").strip().lower(),
    }
    try:
        response = supabase.table("events").insert(payload).execute()
        created = response.data[0] if response.data else payload
        return jsonify(event_with_seat_counts(created)), 201
    except APIError as error:
        return supabase_error_response(error)


@app.get("/api/events")
def list_events():
    try:
        query = supabase.table("events").select("*")
        status = request.args.get("status")
        if status:
            query = query.eq("status", status)
        response = query.execute()
        return jsonify([event_with_seat_counts(event) for event in response.data]), 200
    except APIError as error:
        return supabase_error_response(error)


@app.get("/api/events/<event_id>")
def get_event(event_id):
    event_id = valid_uuid(event_id)
    if not event_id:
        return error_response("event_id must be a valid UUID", 400)
    try:
        response = supabase.table("events").select("*").eq("id", event_id).limit(1).execute()
        if not response.data:
            return error_response("Event not found", 404)
        return jsonify(event_with_seat_counts(response.data[0])), 200
    except APIError as error:
        return supabase_error_response(error)


@app.post("/api/registrations")
def create_registration():
    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        return error_response("Request body must be a JSON object", 400)

    user_id = valid_uuid(body.get("user_id"))
    event_id = valid_uuid(body.get("event_id"))
    if not user_id or not event_id:
        return error_response("user_id and event_id must be valid UUIDs", 400)

    try:
        event_response = supabase.table("events").select("id, capacity, status").eq("id", event_id).limit(1).execute()
        if not event_response.data:
            return error_response("Event not found", 404)

        event = event_response.data[0]
        if str(event.get("status") or "").lower() in {"closed", "cancelled", "canceled", "sold out"}:
            return error_response("Registration is closed for this event", 409)

        existing = supabase.table("registrations").select("id").eq("user_id", user_id).eq("event_id", event_id).limit(1).execute()
        if existing.data:
            return error_response("User is already registered for this event", 409)

        count = supabase.table("registrations").select(
            "id", count="exact", head=True
        ).eq("event_id", event_id).execute().count or 0
        capacity = event.get("capacity")
        if capacity is not None and count >= int(capacity):
            return error_response("Event is full", 409)

        response = supabase.table("registrations").insert({
            "user_id": user_id,
            "event_id": event_id,
        }).execute()
        registration = response.data[0] if response.data else {
            "user_id": user_id,
            "event_id": event_id,
        }
        updated_event = event_with_seat_counts(event)
        return jsonify({
            "registration": registration,
            "event": updated_event,
            "registration_count": updated_event["registration_count"],
            "available_seats": updated_event["available_seats"],
            "is_full": updated_event["is_full"],
        }), 201
    except APIError as error:
        # A unique constraint can still catch simultaneous duplicate requests.
        if getattr(error, "code", None) == "23505":
            return error_response("User is already registered for this event", 409)
        return supabase_error_response(error)


@app.get("/api/me/registrations")
def my_registrations():
    # With authentication disabled, the caller must supply their own user_id.
    user_id = valid_uuid(request.args.get("user_id"))
    if not user_id:
        return error_response("A valid user_id query parameter is required", 400)
    try:
        response = (
            supabase.table("registrations")
            .select("*, events(*)")
            .eq("user_id", user_id)
            .order("created_at", desc=True)
            .execute()
        )
        return jsonify(response.data), 200
    except APIError as error:
        return supabase_error_response(error)


@app.get("/api/events/<event_id>/registrations")
def event_registrations(event_id):
    event_id = valid_uuid(event_id)
    if not event_id:
        return error_response("event_id must be a valid UUID", 400)
    try:
        event = supabase.table("events").select("id, organizer_id").eq("id", event_id).limit(1).execute()
        if not event.data:
            return error_response("Event not found", 404)
        requested_organizer = request.args.get("organizer_id")
        if requested_organizer:
            requested_organizer = valid_uuid(requested_organizer)
            if not requested_organizer:
                return error_response("organizer_id must be a valid UUID", 400)
            if event.data[0].get("organizer_id") != requested_organizer:
                return error_response("This organizer does not own the event", 403)
        response = (
            supabase.table("registrations")
            .select("*, users(id, email)")
            .eq("event_id", event_id)
            .order("created_at")
            .execute()
        )
        return jsonify(response.data), 200
    except APIError as error:
        return supabase_error_response(error)


if __name__ == "__main__":
    app.run(debug=True)



