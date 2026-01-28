import streamlit as st

from run_analysis import generate_full_report


# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="CP Tracker",
    layout="centered"
)

st.title("CP Tracker")
st.write("Backend-first analytics for Codeforces users.")


# -------------------------------
# Session state initialization
# -------------------------------
if "report" not in st.session_state:
    st.session_state.report = None


# -------------------------------
# User input
# -------------------------------
handle = st.text_input("Enter Codeforces username")


# -------------------------------
# Analyze button
# -------------------------------
if st.button("Analyze"):
    if handle.strip():
        st.session_state.report = generate_full_report(handle.strip())
        st.success("Analysis complete!")
    else:
        st.warning("Please enter a username.")


# -------------------------------
# Render results (ONLY if report exists)
# -------------------------------
report = st.session_state.report

if report is not None:

    # ===========================
    # Topic Analysis
    # ===========================
    st.subheader("Topic Analysis")

    topic_rows = []
    for topic, stats in report["topic_analysis"].items():
        attempted = stats["attempted"]
        solved = stats["solved"]
        failed = stats["failed"]
        success_rate = (solved / attempted * 100) if attempted > 0 else 0

        topic_rows.append({
            "Topic": topic,
            "Attempted": attempted,
            "Solved": solved,
            "Failed": failed,
            "Success Rate (%)": round(success_rate, 2)
        })

    st.dataframe(topic_rows, use_container_width=True)


    # ===========================
    # Contest vs Practice Gap
    # ===========================
    st.subheader("Contest vs Practice Gap")
    st.caption("Difference between contest and practice success rates per topic.")

    gap_rows = []
    for topic, stats in report["contest_practice_gap"].items():
        gap_rows.append({
            "Topic": topic,
            "Contest Success Rate": round(stats["contest_success_rate"], 2),
            "Practice Success Rate": round(stats["practice_success_rate"], 2),
            "Gap (Practice - Contest)": round(stats["gap"], 2)
        })

    st.dataframe(gap_rows, use_container_width=True)


    # ===========================
    # Difficulty Analysis
    # ===========================
    st.subheader("Difficulty Analysis")

    difficulty_rows = []
    for bucket, stats in report["difficulty_analysis"].items():
        difficulty_rows.append({
            "Difficulty Range": bucket,
            "Attempted": stats["attempted"],
            "Solved": stats["solved"],
            "Failed": stats["failed"],
            "Success Rate": round(stats["success_rate"], 2)
        })

    st.dataframe(difficulty_rows, use_container_width=True)
