import streamlit as st
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

        st.subheader("Topic Analysis")
        st.json(report["topic_analysis"])

        st.subheader("Weak Topics")
        st.json(report["weak_topics"])

        st.subheader("Difficulty Analysis")
        st.json(report["difficulty_analysis"])
