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


@app.get("/")
def index():
    return jsonify({"message": "Events API", "endpoints": [
        "GET /api/events",
        "GET /api/events/<event_id>",
        "POST /api/registrations",
        "GET /api/me/registrations?user_id=<user_id>",
        "GET /api/events/<event_id>/registrations",
    ]})


@app.get("/api/events")
def list_events():
    try:
        query = supabase.table("events").select("*")
        status = request.args.get("status")
        if status:
            query = query.eq("status", status)
        response = query.execute()
        return jsonify(response.data), 200
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
        return jsonify(response.data[0]), 200
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
        event_response = supabase.table("events").select("id, capacity").eq("id", event_id).limit(1).execute()
        if not event_response.data:
            return error_response("Event not found", 404)

        event = event_response.data[0]
        existing = supabase.table("registrations").select("id").eq("user_id", user_id).eq("event_id", event_id).execute()
        if existing.data:
            return error_response("User is already registered for this event", 409)

        capacity = event.get("capacity")
        if capacity is not None:
            registrations = supabase.table("registrations").select("id").eq("event_id", event_id).execute()
            if len(registrations.data) >= int(capacity):
                return error_response("Event is full", 409)

        response = supabase.table("registrations").insert({
            "user_id": user_id,
            "event_id": event_id,
        }).execute()
        registration = response.data[0] if response.data else {
            "user_id": user_id,
            "event_id": event_id,
        }
        return jsonify(registration), 201
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
        event = supabase.table("events").select("id").eq("id", event_id).limit(1).execute()
        if not event.data:
            return error_response("Event not found", 404)
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
