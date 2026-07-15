# cp_tracker 📊

A full-stack competitive programming analytics tool that turns raw Codeforces submission history into clear, actionable insights. It pulls live data from the Codeforces API and analyzes performance across topics, difficulty levels, and contest-vs-practice patterns — styled as a terminal, because that's where this data actually lives.

Originally built as a Streamlit app, cp_tracker has since been rearchitected into a proper full-stack application with a **FastAPI backend** and a **React (Vite) frontend**.

## Features

- **Topic Performance Analysis** — solved vs failed problems broken down by topic tag
- **Weak Topic Detection** — automatically flags topics where success rate is low
- **Difficulty Breakdown** — performance grouped by problem rating ranges
- **Contest vs Practice Gap** — compares success rate in live contests vs practice submissions, per topic
- **Rating Progression** — visualizes rating change over every rated contest, colored by current Codeforces rank tier
- **Problem Recommendations** — suggests unsolved problems in weak topics, matched to current rating and color-coded using Codeforces' own rank-color convention (gray → green → cyan → blue → purple → orange → red)

## Design

The UI is framed as a terminal window — traffic-light dots, a `zsh` title bar, and a shell-prompt-styled search (`cf analyze <handle>`) — since that's the native environment for the audience this tool is built for. Every rating value on the page (recommended problems, the rating chart) uses the exact color scale Codeforces itself uses for ranks, so a color always means the same thing here as it does on the real site.

- Typography: JetBrains Mono (headers, data, labels) + Inter (body text)
- Palette: near-black terminal background, AC-green (`#2ea043`) / WA-red (`#e5484d`) verdict colors, and the full 7-tier Codeforces rank-color scale

## Tech Stack

**Backend**
- FastAPI (Python)
- Uvicorn (ASGI server)
- Requests (Codeforces API client)

**Frontend**
- React (Vite)
- Axios (API calls)
- Recharts (data visualization)

## Project Structure

```
cp-tracker/
├── backend/
│   ├── main.py                  # FastAPI app entrypoint
│   ├── routers/
│   │   └── analysis.py          # /analyze/{handle} endpoints
│   ├── services/
│   │   ├── analysis/            # topic, difficulty, weak-topic, contest-gap analysis
│   │   ├── api/
│   │   │   └── codeforces.py    # Codeforces API client
│   │   ├── recommender/
│   │   │   └── suggest.py       # problem recommendation logic
│   │   └── run_analysis.py      # aggregates all analysis into one report
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── client.js        # backend API client
│   │   ├── components/          # chart & UI components
│   │   ├── pages/
│   │   │   └── Dashboard.jsx    # main dashboard page
│   │   ├── utils/
│   │   │   └── ratingColor.js   # Codeforces rank-color mapping
│   │   ├── App.jsx
│   │   └── App.css
│   └── package.json
│
├── render.yaml                  # Render deployment config
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+

### Backend Setup

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload
```

The API will be running at `http://localhost:8000`. Interactive API docs are available at `http://localhost:8000/docs`.

### Frontend Setup

In a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

The app will be running at `http://localhost:5173`.

### Usage

1. Start both the backend and frontend servers (see above)
2. Open `http://localhost:5173` in your browser
3. Enter any Codeforces handle (e.g. `tourist`) and hit **run**
4. View topic performance, weak topics, difficulty breakdown, rating progression, and recommended problems

## Live Demo

- **Frontend:** [cp-tracker-green.vercel.app](https://cp-tracker-green.vercel.app)
- **Backend API:** [cp-tracker-api-brco.onrender.com](https://cp-tracker-api-brco.onrender.com)

Note: the backend runs on Render's free tier, which spins down after inactivity — the first request after idle time can take 30-50 seconds to wake up.

## API Reference

### `GET /analyze/{handle}`

Returns a full analytics report for the given Codeforces handle.

**Example:** `GET /analyze/tourist`

**Response:**
```json
{
  "topic_analysis": { "dp": { "attempted": 318, "solved": 242, "failed": 76 } },
  "weak_topics": { "interactive": { "attempted": 98, "solved": 41, "success_rate": 0.42 } },
  "difficulty_analysis": { "800-900": { "attempted": 94, "solved": 88, "failed": 6 } },
  "contest_practice_gap": { "dp": { "contest_success_rate": 0.75, "practice_success_rate": 0.78, "gap": 0.03 } }
}
```

### `GET /analyze/{handle}/recommendations`

Returns unsolved problem recommendations for the handle's weak topics, calibrated to their current rating.

**Response:**
```json
{
  "interactive": [
    { "name": "Problem Name", "rating": 1500, "tags": ["interactive", "dp"], "url": "https://codeforces.com/problemset/problem/.../..." }
  ]
}
```

### `GET /analyze/{handle}/rating-history`

Returns contest-by-contest rating changes for the handle.

**Response:**
```json
[
  { "contest": "Codeforces Round 900", "date": 1700000000, "rating": 2100, "change": 34 }
]
```

## Deployment

### Backend (Render)

A `render.yaml` is included at the repo root — connect the repo in the [Render dashboard](https://dashboard.render.com) and it will pick up the build/start commands automatically. Set the `ALLOWED_ORIGINS` env var to your deployed frontend URL (comma-separated if more than one).

Manually, the equivalent commands are:
```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

### Frontend (Vercel)

1. Import the repo in Vercel, set **Root Directory** to `frontend`
2. Framework preset: Vite (auto-detected)
3. Add an env var `VITE_API_URL` pointing to your deployed backend URL (e.g. `https://cp-tracker-api-brco.onrender.com`)
4. Deploy — Vercel runs `npm install && npm run build` automatically

### Local env config

Copy `frontend/.env.example` to `frontend/.env` and adjust `VITE_API_URL` if your backend isn't on `localhost:8000`.

## Roadmap

- [x] Wire up the problem recommendation endpoint (`suggest.py`) to the frontend
- [x] Add loading skeletons and improved error states
- [x] Deploy backend (Render) and frontend (Vercel) — live and public
- [x] Add rating progression chart over time
- [x] Redesign UI with a terminal aesthetic and Codeforces rank-color system

## License

This project is for educational/personal use.
