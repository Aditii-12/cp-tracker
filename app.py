import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timezone

from run_analysis import generate_full_report
from api.codeforces import get_rating_history, get_user_info, get_submissions
from recommender.suggest import recommend_problems

st.set_page_config(page_title="CP Tracker", layout="wide", page_icon="🏆")

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at 20% 20%, rgba(99,102,241,0.15), transparent 40%),
                radial-gradient(circle at 80% 80%, rgba(139,92,246,0.15), transparent 40%),
                linear-gradient(135deg, #0f172a, #111827);
}
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 8px;
    border: none;
    padding: 0.5rem 1.3rem;
    font-weight: 600;
}
.stButton>button:hover { opacity: 0.9; }
.metric-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

if "report" not in st.session_state:
    st.session_state.report = None
if "handle" not in st.session_state:
    st.session_state.handle = ""

st.title("🏆 CP Tracker")
st.caption("Competitive programming analytics for Codeforces users.")

col_input, col_btn = st.columns([4, 1])
with col_input:
    handle = st.text_input("Codeforces Username", placeholder="e.g. tourist", label_visibility="collapsed")
with col_btn:
    analyze = st.button("Analyze", use_container_width=True)

if analyze:
    if not handle:
        st.warning("Please enter a Codeforces username.")
    else:
        with st.spinner("Fetching and analyzing data..."):
            st.session_state.report = generate_full_report(handle)
            st.session_state.handle = handle
        st.success("Analysis complete!")

report = st.session_state.report
stored_handle = st.session_state.handle

if report is not None:

    # ── User Info Banner ──────────────────────────────────────────────────────
    try:
        info = get_user_info(stored_handle)
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Handle", info.get("handle", stored_handle))
        with c2:
            st.metric("Rating", info.get("rating", "Unrated"))
        with c3:
            st.metric("Max Rating", info.get("maxRating", "N/A"))
        with c4:
            st.metric("Rank", info.get("rank", "N/A").title())
    except Exception:
        pass

    st.divider()

    tabs = st.tabs(["📊 Topic Analysis", "📈 Rating History", "🔥 Solve Heatmap", "💡 Recommendations", "🎯 Difficulty"])

    # ── Tab 1: Topic Analysis ─────────────────────────────────────────────────
    with tabs[0]:
        st.subheader("Topic-wise Performance")
        topic_data = report.get("topic_analysis", {})
        if topic_data:
            rows = []
            for topic, stats in topic_data.items():
                rate = round((stats["solved"] / stats["attempted"]) * 100, 1) if stats["attempted"] > 0 else 0
                rows.append({"Topic": topic, "Attempted": stats["attempted"], "Solved": stats["solved"],
                              "Failed": stats["failed"], "Success Rate (%)": rate})
            df = pd.DataFrame(rows).sort_values("Attempted", ascending=False)
            st.dataframe(df, use_container_width=True, hide_index=True)

            fig = px.bar(df.head(15), x="Topic", y=["Solved", "Failed"],
                         barmode="stack", title="Top 15 Topics — Solved vs Failed",
                         color_discrete_map={"Solved": "#6366f1", "Failed": "#ef4444"})
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                               font_color="white", xaxis_tickangle=-30)
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Weak Topics")
        weak_topics = report.get("weak_topics", {})
        if weak_topics:
            wrows = []
            for topic, stats in weak_topics.items():
                wrows.append({"Topic": topic, "Attempted": stats["attempted"], "Solved": stats["solved"],
                               "Success Rate (%)": round(stats["success_rate"] * 100, 1)})
            wdf = pd.DataFrame(wrows).sort_values("Success Rate (%)")
            st.dataframe(wdf, use_container_width=True, hide_index=True)

            fig2 = px.bar(wdf, x="Topic", y="Success Rate (%)", title="Weak Topics — Success Rate",
                          color="Success Rate (%)", color_continuous_scale="RdYlGn")
            fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.success("No weak topics detected 🎉")

    # ── Tab 2: Rating History ─────────────────────────────────────────────────
    with tabs[1]:
        st.subheader("Rating History")
        try:
            history = get_rating_history(stored_handle)
            if history:
                rdf = pd.DataFrame([{
                    "Contest": h["contestName"],
                    "Date": datetime.fromtimestamp(h["ratingUpdateTimeSeconds"], tz=timezone.utc).strftime("%Y-%m-%d"),
                    "Rating": h["newRating"],
                    "Change": h["newRating"] - h["oldRating"]
                } for h in history])

                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=rdf["Date"], y=rdf["Rating"],
                    mode="lines+markers",
                    line=dict(color="#6366f1", width=2),
                    marker=dict(size=6, color=rdf["Change"].apply(lambda x: "#22c55e" if x >= 0 else "#ef4444")),
                    hovertemplate="<b>%{customdata}</b><br>Rating: %{y}<extra></extra>",
                    customdata=rdf["Contest"]
                ))
                fig.update_layout(
                    title="Rating Over Time",
                    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                    font_color="white", xaxis_title="Date", yaxis_title="Rating",
                    hovermode="x unified"
                )
                st.plotly_chart(fig, use_container_width=True)

                best = rdf.loc[rdf["Rating"].idxmax()]
                worst = rdf.loc[rdf["Change"].idxmin()]
                c1, c2, c3 = st.columns(3)
                c1.metric("Peak Rating", best["Rating"])
                c2.metric("Total Contests", len(rdf))
                c3.metric("Biggest Drop", worst["Change"], delta_color="inverse")
            else:
                st.info("No contest history found for this user.")
        except Exception as e:
            st.error(f"Could not fetch rating history: {e}")

    # ── Tab 3: Solve Heatmap ──────────────────────────────────────────────────
    with tabs[2]:
        st.subheader("Solve Activity Heatmap")
        try:
            submissions = get_submissions(stored_handle)
            ac_subs = [s for s in submissions if s["verdict"] == "OK"]
            if ac_subs:
                dates = [datetime.fromtimestamp(s["creationTimeSeconds"], tz=timezone.utc).date() for s in ac_subs]
                date_counts = pd.Series(dates).value_counts().reset_index()
                date_counts.columns = ["date", "count"]
                date_counts["date"] = pd.to_datetime(date_counts["date"])
                date_counts["week"] = date_counts["date"].dt.isocalendar().week.astype(str) + "-" + date_counts["date"].dt.year.astype(str)
                date_counts["weekday"] = date_counts["date"].dt.day_name()
                date_counts["month"] = date_counts["date"].dt.strftime("%b %Y")

                fig = px.density_heatmap(
                    date_counts, x="month", y="weekday",
                    z="count", color_continuous_scale="Purples",
                    title="Solve Frequency by Day of Week & Month",
                    category_orders={"weekday": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]}
                )
                fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
                st.plotly_chart(fig, use_container_width=True)

                c1, c2, c3 = st.columns(3)
                c1.metric("Total AC Submissions", len(ac_subs))
                c2.metric("Active Days", date_counts["date"].nunique())
                best_day = date_counts.loc[date_counts["count"].idxmax()]
                c3.metric("Best Day", f"{best_day['count']} solves")
            else:
                st.info("No accepted submissions found.")
        except Exception as e:
            st.error(f"Could not fetch submissions: {e}")

    # ── Tab 4: Recommendations ───────────────────────────────────────────────
    with tabs[3]:
        st.subheader("💡 Smart Problem Recommendations")
        st.caption("Problems picked from your weak topics, calibrated to your rating.")

        weak_topics = report.get("weak_topics", {})
        if not weak_topics:
            st.success("No weak topics detected — you're solid across all areas! 🎉")
        else:
            with st.spinner("Finding the right problems for you..."):
                recs = recommend_problems(stored_handle, weak_topics)

            if not recs:
                st.info("No unsolved problems found in the target range. Try solving more to unlock recommendations.")
            else:
                for topic, problems in recs.items():
                    with st.expander(f"🔖 {topic.title()} — {len(problems)} problems", expanded=True):
                        for p in problems:
                            cols = st.columns([5, 1, 2])
                            cols[0].markdown(f"**[{p['name']}]({p['url']})**")
                            cols[1].markdown(f"⭐ `{p['rating']}`")
                            cols[2].markdown(" ".join([f"`{t}`" for t in p['tags'][:3]]))

    # ── Tab 5: Difficulty ────────────────────────────────────────────────────
    with tabs[4]:
        st.subheader("Difficulty-wise Performance")
        difficulty_data = report.get("difficulty_analysis", {})
        if difficulty_data:
            rows = []
            for bucket, stats in difficulty_data.items():
                rows.append({"Difficulty Range": bucket, "Attempted": stats["attempted"],
                              "Solved": stats["solved"], "Failed": stats["failed"],
                              "Success Rate (%)": round(stats["success_rate"] * 100, 1)})
            ddf = pd.DataFrame(rows)
            st.dataframe(ddf, use_container_width=True, hide_index=True)

            fig = px.bar(ddf, x="Difficulty Range", y="Success Rate (%)",
                         color="Success Rate (%)", color_continuous_scale="RdYlGn",
                         title="Success Rate by Difficulty")
            fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Contest vs Practice Gap")
        gap_data = report.get("contest_practice_gap", {})
        if gap_data:
            grows = []
            for topic, stats in gap_data.items():
                grows.append({"Topic": topic,
                               "Contest (%)": round(stats["contest_success_rate"] * 100, 1),
                               "Practice (%)": round(stats["practice_success_rate"] * 100, 1),
                               "Gap": round(stats["gap"] * 100, 1)})
            gdf = pd.DataFrame(grows).sort_values("Gap", ascending=False)
            st.dataframe(gdf, use_container_width=True, hide_index=True)
        else:
            st.info("Contest vs practice data not available.")