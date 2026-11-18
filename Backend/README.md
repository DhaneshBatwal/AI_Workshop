# Events API

Flask API backed by Supabase. Render uses `render.yaml` to build and start the service.

## Routes

- `GET /api/events` and `GET /api/events/<event_id>` browse events.
- `POST /api/events` creates an event from `title`, `organizer_id`, optional `capacity`, and `status`.
- `POST /api/registrations` creates an attendee registration.
- `GET /api/me/registrations?user_id=<uuid>` returns one user’s registrations.
- `GET /api/events/<event_id>/registrations` returns an event roster. Supplying `organizer_id` checks that it matches the event owner for the Organizer UI.

The current schema does not have event date, venue, or description columns. Role switching in the frontend is presentation-only; without authentication, IDs can be spoofed and API access remains public.

## Deploy on Render

1. Connect the repository and use `Backend` as the service root directory (or make this folder the repository root).
2. Create a Blueprint from `render.yaml`, or create a Python Web Service with the commands below.
3. Set `SUPABASE_URL` and `SUPABASE_PUBLISHABLE_KEY` in the Render service environment. Do not upload `.env`.
4. Deploy. The health check is `GET /`.

Build command: `pip install -r requirements.txt`

Start command: `gunicorn app:app`
