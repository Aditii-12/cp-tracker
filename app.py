import streamlit as st

st.set_page_config(page_title="CP Tracker", layout="centered")

st.title("CP Tracker")
st.write("Backend-first analytics for Codeforces users.")

handle = st.text_input("Enter Codeforces username")

if st.button("Submit"):
    if handle:
        st.success(f"Username received: {handle}")
    else:
        st.warning("Please enter a username.")
