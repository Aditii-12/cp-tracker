# CP Tracker 📊

**CP Tracker** is a competitive programming analytics tool that turns your raw Codeforces submission history into clear, actionable insights. It pairs a standalone analytics backend with an interactive Streamlit dashboard, so you can see exactly where you're strong, where you're weak, and how you perform under contest pressure versus casual practice.

---

## Why CP Tracker?

Most competitive programmers know their rating, but few can answer questions like:

- *Which topics am I actually weak in — not just which ones I avoid?*
- *Do I perform worse in contests than in practice, and by how much?*
- *At which difficulty range does my success rate start dropping off?*

CP Tracker answers these by pulling your real submission data from the Codeforces public API and breaking it down across multiple dimensions — topic, difficulty, and contest vs. practice — instead of relying on a single rating number.

---

## Key Features

- 🧩 **Topic-wise analysis** — attempted, solved, failed, and success rate for every tag (DP, greedy, math, implementation, etc.)
- 🎯 **Weak topic detection** — automatically flags topics with low success rates
- 📈 **Difficulty-wise breakdown** — performance across rating buckets (800–900, 1000–1100, ...)
- ⚔️ **Contest vs. practice gap analysis** — quantifies how much pressure affects your solve rate
- 🔌 **Decoupled analytics engine** — the backend runs independently of the UI, so it can be reused in a CLI, script, or another frontend
- 🖥️ **Interactive Streamlit dashboard** — enter a Codeforces handle and get live visual analysis

---

## Project Structure

```
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

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### 1. Clone the repository

```bash
git clone https://github.com/Aditii-12/cp-tracker.git
cd cp-tracker
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit dashboard

```bash
streamlit run app.py
```

### 5. Analyze a Codeforces user

Enter any Codeforces handle in the dashboard and click **Analyze** to view:
- Topic-wise performance
- Weak topics
- Difficulty-level breakdown
- Contest vs. practice gap

> No authentication required — CP Tracker only uses the public Codeforces API.

---

## Running Analysis Without the UI

The analytics engine is fully decoupled from the dashboard, so you can also generate a report directly from the command line:

```bash
python run_analysis.py
```

This is useful if you want to script CP Tracker, feed its output into another tool, or build a different frontend on top of it.

---

## Roadmap / Ideas for Extension

- [ ] Historical trend tracking (rating and success rate over time)
- [ ] Comparison mode between two handles
- [ ] Export reports as PDF/CSV
- [ ] Support for other judges (Codechef, AtCoder)

Contributions and suggestions are welcome — feel free to open an issue or PR.

---

## Author

**Aditi Sahu**
Integrated B.Tech + M.Tech, ABV-IIITM Gwalior
