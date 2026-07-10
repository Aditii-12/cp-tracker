# CP Tracker 📊

CP Tracker is a full-stack competitive programming analytics tool that turns your raw Codeforces submission history into clear, actionable insights. It pulls live data from the Codeforces API and analyzes your performance across topics, difficulty levels, and contest-vs-practice patterns.

Originally built as a Streamlit app, CP Tracker has since been rearchitected into a proper full-stack application with a **FastAPI backend** and a **React (Vite) frontend**.

## Features

- **Topic Performance Analysis** — see solved vs failed problems broken down by topic tag
- **Weak Topic Detection** — automatically flags topics where your success rate is low
- **Difficulty Breakdown** — performance grouped by problem rating ranges
- **Contest vs Practice Gap** — compares your success rate in live contests vs practice submissions, per topic
- **Problem Recommendations** — suggests unsolved problems in your weak topics, matched to your current rating

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
│   │   └── analysis.py          # /analyze/{handle} endpoint
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
│   │   ├── App.jsx
│   │   └── App.css
│   └── package.json
│
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
3. Enter any Codeforces handle (e.g. `tourist`) and click **Analyze**
4. View topic performance, weak topics, difficulty breakdown, and contest-vs-practice gap

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

## Roadmap

- [ ] Wire up the problem recommendation endpoint (`suggest.py`) to the frontend
- [ ] Add loading skeletons and improved error states
- [ ] Deploy backend (Render/Railway) and frontend (Vercel/Netlify)
- [ ] Add rating progression chart over time

## License

This project is for educational/personal use.