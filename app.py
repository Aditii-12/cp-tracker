import streamlit as st
from run_analysis import generate_full_report

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(page_title="CP Tracker", layout="centered")

# --------------------------------------------------
# Session state initialization
# --------------------------------------------------
if "report" not in st.session_state:
    st.session_state.report = None

# --------------------------------------------------
# UI Header
# --------------------------------------------------
st.title("CP Tracker")
st.caption("Backend-first analytics for Codeforces users.")

handle = st.text_input("Enter Codeforces username")

# --------------------------------------------------
# Analyze Button
# --------------------------------------------------
if st.button("Analyze"):
    if not handle:
        st.warning("Please enter a Codeforces username.")
    else:
        with st.spinner("Analyzing submissions..."):
            st.session_state.report = generate_full_report(handle)
        st.success("Analysis complete!")

# --------------------------------------------------
# Render results ONLY if report exists
# --------------------------------------------------
report = st.session_state.report

if report is not None:

    # ==================================================
    # Topic Analysis
    # ==================================================
    st.subheader("Topic Analysis")

    topic_data = report.get("topic_analysis", {})

    if topic_data:
        rows = []
        for topic, stats in topic_data.items():
            rows.append({
                "Topic": topic,
                "Attempted": stats["attempted"],
                "Solved": stats["solved"],
                "Failed": stats["failed"],
                "Success Rate (%)": round(
                    (stats["solved"] / stats["attempted"]) * 100, 2
                ) if stats["attempted"] > 0 else 0
            })

        st.dataframe(rows, use_container_width=True)
    else:
        st.info("No topic data available.")

    # ==================================================
    # Weak Topics
    # ==================================================
    st.subheader("Weak Topics")
    st.caption("Topics with low success rate based on past submissions.")

    weak_topics = report.get("weak_topics", {})

    if weak_topics:
        rows = []
        for topic, stats in weak_topics.items():
            rows.append({
                "Topic": topic,
                "Attempted": stats["attempted"],
                "Solved": stats["solved"],
                "Failed": stats["failed"],
                "Success Rate (%)": round(stats["success_rate"] * 100, 2)
            })

        st.dataframe(rows, use_container_width=True)
    else:
        st.success("No weak topics detected 🎉")

    # ==================================================
    # Contest vs Practice Gap
    # ==================================================
    st.subheader("Contest vs Practice Gap")
    st.caption("Difference between practice and contest success rates per topic.")

    gap_data = report.get("contest_practice_gap", {})

    if gap_data:
        rows = []
        for topic, stats in gap_data.items():
            rows.append({
                "Topic": topic,
                "Contest Success (%)": round(stats["contest_success_rate"] * 100, 2),
                "Practice Success (%)": round(stats["practice_success_rate"] * 100, 2),
                "Gap (Practice − Contest)": round(stats["gap"] * 100, 2)
            })

        st.dataframe(rows, use_container_width=True)
    else:
        st.info("Contest vs practice data not available.")

    # ==================================================
    # Difficulty Analysis
    # ==================================================
    st.subheader("Difficulty-wise Performance")

    difficulty_data = report.get("difficulty_analysis", {})

    if difficulty_data:
        rows = []
        for bucket, stats in difficulty_data.items():
            rows.append({
                "Difficulty Range": bucket,
                "Attempted": stats["attempted"],
                "Solved": stats["solved"],
                "Failed": stats["failed"],
                "Success Rate (%)": round(stats["success_rate"] * 100, 2)
            })

        st.dataframe(rows, use_container_width=True)
    else:
        st.info("Difficulty analysis not available.")
