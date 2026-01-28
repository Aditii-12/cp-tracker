import streamlit as st
import pandas as pd
import run_analysis

st.set_page_config(page_title="CP Tracker", layout="centered")

st.title("CP Tracker")
st.write("Backend-first analytics for Codeforces users.")

handle = st.text_input("Enter Codeforces username")

if st.button("Analyze"):
    if not handle:
        st.warning("Please enter a username.")
    else:
        with st.spinner("Fetching data from Codeforces..."):
            report = run_analysis.generate_full_report(handle)

        st.success("Analysis complete!")

        # =======================
        # Topic Analysis (TABLE)
        # =======================
        st.subheader("Topic Analysis")

        topic_data = []
        for topic, stats in report["topic_analysis"].items():
            attempted = stats["attempted"]
            solved = stats["solved"]
            failed = stats["failed"]
            success_rate = round((solved / attempted) * 100, 2) if attempted > 0 else 0

            topic_data.append({
                "Topic": topic,
                "Attempted": attempted,
                "Solved": solved,
                "Failed": failed,
                "Success Rate (%)": success_rate
            })

        df_topics = pd.DataFrame(topic_data)
        df_topics = df_topics.sort_values(by="Attempted", ascending=False)

        st.dataframe(df_topics, use_container_width=True)

        # =======================
        # Weak Topics (RAW for now)
        # =======================
        st.subheader("Weak Topics")
        st.json(report["weak_topics"])

        # =======================
        # Difficulty Analysis (RAW for now)
        # =======================
        st.subheader("Difficulty Analysis")
        st.json(report["difficulty_analysis"])
