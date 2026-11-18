# CampusHub Frontend

React + Vite frontend matched to the four CampusHub references in `../Design`, using the palette and type from `campus_linear/DESIGN.md`.

## Run locally

```bash
npm install
npm run dev
```

The frontend calls `https://ai-workshop-06p4.onrender.com` by default. Set `VITE_API_BASE_URL` (for example by copying `.env.example` to `.env`) to use another API.

## Views and endpoints

- Student: `GET /api/events`, `GET /api/events/{id}`, `POST /api/registrations`, and `GET /api/me/registrations?user_id=...`.
- Organizer: the student event flow, `POST /api/events`, and `GET /api/events/{id}/registrations?organizer_id=...` for events matching the entered organizer UUID. Roster search and CSV export run in the browser.
- Admin: all events plus registration rosters fetched through `GET /api/events/{id}/registrations`.

## Current database limits

The schema stores event title, organizer UUID, capacity, and status, and registration user/event UUIDs plus creation time. Event date, venue, and description are not persisted. The UI labels these as unavailable and doesn’t send unknown columns to Supabase.

Role switching is a client-side view only. There is no authentication, so organizer ownership checks and the Admin view are not secure access controls; direct API requests remain public. The updated `Backend/app.py` adds `POST /api/events`; redeploy the backend before using event creation on the Render API.

## Build

`npm run build` creates `dist/` for static hosting.
