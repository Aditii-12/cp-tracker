# CP Tracker

CP Tracker is a backend-driven analytics system that analyzes competitive programming performance using the Codeforces public API.  
It processes real submission data to extract topic-wise, difficulty-wise, and contest-based performance insights.

---

## What This Project Does

- Fetches real submission data from Codeforces for any user
- Analyzes performance across multiple dimensions:
  - Problem topics (dp, greedy, math, etc.)
  - Problem difficulty levels
  - Contest vs practice performance
- Identifies weak and strong areas based on success-rate analysis
- Generates a unified analytics report that can later be consumed by a UI or API

---

## Key Features

- Topic-wise performance analysis  
- Weak / strong topic classification  
- Difficulty-wise performance analysis  
- Contest vs practice gap analysis  
- Unified backend report generator  

---

## Project Structure

```text
cp-tracker/
├── api/
│   └── codeforces.py          # Codeforces API integration
├── analysis/
│   ├── topic_analysis.py      # Topic-wise aggregation
│   ├── weak_topic_analysis.py # Weak/strong classification
│   ├── difficulty_analysis.py # Difficulty-based analysis
│   ├── contest_practice_gap.py# Contest vs practice comparison
│   └── aggregate_report.py    # Unified analytics report
├── run_analysis.py            # Backend runner script
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### 1. Activate virtual environment

```bash
source venv/bin/activate
```

### 2. Run backend analysis

```bash
python run_analysis.py
```

### 3. Analyze a different Codeforces user

Edit `run_analysis.py`:

```python
HANDLE = "your_codeforces_handle"
```

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
