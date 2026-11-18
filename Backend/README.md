# Events API

Flask API backed by Supabase. Render uses `render.yaml` to build and start the service.

## Deploy on Render

1. Push this `Backend` folder as the root of a Git repository, or configure it as the service root directory in your existing repository.
2. In Render, create a Blueprint from that repository (or create a Python Web Service with the commands below).
3. Set `SUPABASE_URL` and `SUPABASE_PUBLISHABLE_KEY` in the Render service environment. Do not upload `.env`; it is excluded by `.gitignore`.
4. Deploy. The health check is `GET /`.

Build command: `pip install -r requirements.txt`

Start command: `gunicorn app:app`

The API endpoints are listed by `GET /`. The existing API has no authentication and uses wildcard CORS; keep that in mind before exposing real user data publicly.
