# CP Tracker

CP Tracker is a competitive programming analytics system that analyzes Codeforces performance using real submission data.  
It combines a **robust analytics backend** with an **interactive Streamlit dashboard** to help users understand their strengths, weaknesses, and performance patterns.

---

## What This Project Does

- Fetches real submission data from the Codeforces public API
- Analyzes hundreds of submissions for a given user
- Breaks performance down across multiple dimensions:
  - Topic-wise (greedy, dp, math, implementation, etc.)
  - Difficulty-wise (rating buckets such as 800–900, 1000–1100)
  - Contest vs practice performance
- Identifies weak topics using success-rate analysis
- Computes contest vs practice performance gaps
- Displays all insights through a Streamlit-based dashboard

---

## Key Features

- **Topic-wise analysis**: attempted, solved, failed, and success rate per topic  
- **Weak topic detection** based on low success rates  
- **Difficulty-wise performance analysis** across rating buckets  
- **Contest vs practice gap analysis** to measure performance under pressure  
- **Unified analytics backend** independent of the UI  
- **Interactive Streamlit dashboard** for live analysis using a username input  

---

## Project Structure

```text
cp-tracker/
├── api/
│   └── codeforces.py            # Codeforces API integration
├── analysis/
│   ├── topic_analysis.py        # Topic-wise aggregation
│   ├── weak_topic_analysis.py   # Weak topic detection
│   ├── difficulty_analysis.py   # Difficulty-based analysis
│   ├── contest_practice_gap.py  # Contest vs practice comparison
│   └── aggregate_report.py      # Unified analytics report
├── run_analysis.py              # Backend report generator (CLI + UI)
├── app.py                       # Streamlit dashboard
├── requirements.txt
└── README.md
```

---


## How to Run the Project

### 1. Activate virtual environment

```bash
source venv/bin/activate
```

### 2. Install dependencies (first time only)

```bash
pip install -r requirements.txt
```

### 3. Run Streamlit dashboard


```python
streamlit run app.py

```

### 4. Analyze a Codeforces user
- Enter the Codeforces handle directly in the Streamlit UI
- Click Analyze to view topic analysis, weak topics, difficulty performance, and contest gaps

---

## Notes

- Uses Codeforces public API (no authentication required)
- Designed as a backend analytics engine
- Easily extendable for UI or web dashboard integration

---

## Author

Aditi Sahu  
Integrated B.Tech + M.Tech  
ABV-IIITM Gwalior
