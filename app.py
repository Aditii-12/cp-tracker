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

        st.caption("Topics with low success rate — focus on these to improve fastest.")

        weak_data = []
        for topic, stats in report["weak_topics"].items():
            weak_data.append({
                "Topic": topic,
                "Attempted": stats["attempted"],
                "Solved": stats["solved"],
                "Failed": stats["failed"],
                "Success Rate (%)": round(stats["success_rate"] * 100, 2)
            })

        if weak_data:
            st.write(f"You have **{len(weak_data)} weak topics** that need attention.")
    
            df_weak = pd.DataFrame(weak_data)
            df_weak = df_weak.sort_values(by="Success Rate (%)")
            st.dataframe(df_weak, use_container_width=True)
        else:
            st.write("No weak topics found 🎉")



        # =======================
        # Difficulty Analysis (RAW for now)
        # =======================
        st.subheader("Difficulty Analysis")
        st.json(report["difficulty_analysis"])
