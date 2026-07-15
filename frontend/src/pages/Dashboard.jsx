import { useState } from "react";
import { fetchAnalysis, fetchRecommendations, fetchRatingHistory } from "../api/client";
import HandleForm from "../components/HandleForm";
import TopicChart from "../components/TopicChart";
import WeakTopicsList from "../components/WeakTopicsList";
import DifficultyChart from "../components/DifficultyChart";
import ContestGapChart from "../components/ContestGapChart";
import RatingChart from "../components/RatingChart";
import RecommendationsList from "../components/RecommendationsList";

export default function Dashboard() {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const [recommendations, setRecommendations] = useState(null);
  const [recLoading, setRecLoading] = useState(false);
  const [recError, setRecError] = useState(null);

  const [ratingHistory, setRatingHistory] = useState(null);
  const [ratingLoading, setRatingLoading] = useState(false);
  const [ratingError, setRatingError] = useState(null);

  const handleAnalyze = async (handle) => {
    setLoading(true);
    setError(null);
    setReport(null);
    setRecommendations(null);
    setRecError(null);
    setRatingHistory(null);
    setRatingError(null);

    try {
      const data = await fetchAnalysis(handle);
      setReport(data);
    } catch (err) {
      setError(
        err.response?.data?.detail || "Something went wrong. Check the handle."
      );
      setLoading(false);
      return;
    }
    setLoading(false);

    setRecLoading(true);
    fetchRecommendations(handle)
      .then(setRecommendations)
      .catch((err) =>
        setRecError(err.response?.data?.detail || "Could not load recommendations.")
      )
      .finally(() => setRecLoading(false));

    setRatingLoading(true);
    fetchRatingHistory(handle)
      .then(setRatingHistory)
      .catch((err) =>
        setRatingError(err.response?.data?.detail || "Could not load rating history.")
      )
      .finally(() => setRatingLoading(false));
  };

  return (
    <div className="dashboard">
      <div className="terminal">
        <div className="terminal-bar">
          <span className="terminal-dot red" />
          <span className="terminal-dot yellow" />
          <span className="terminal-dot green" />
          <span className="terminal-title">cp-tracker — zsh</span>
        </div>

        <div className="terminal-body">
          <div className="brand">
            <p className="brand-eyebrow">codeforces submission analytics</p>
            <h1>
              cp<span>_</span>tracker
            </h1>
          </div>

          <HandleForm onSubmit={handleAnalyze} loading={loading} />
          {!report && !loading && !error && (
            <p className="hint">enter a handle and press run to pull live stats</p>
          )}

          {error && <p className="error">✗ {error}</p>}

          {loading && (
            <div className="report-grid">
              <div className="chart-card">
                <h3>topic performance</h3>
                <div className="skeleton skeleton-chart" />
              </div>
              <div className="chart-card">
                <h3>weak topics</h3>
                <div className="skeleton skeleton-list" />
              </div>
            </div>
          )}

          {report && (
            <div className="report-grid">
              <TopicChart topicAnalysis={report.topic_analysis} />
              <WeakTopicsList weakTopics={report.weak_topics} />
              <DifficultyChart difficultyAnalysis={report.difficulty_analysis} />
              <ContestGapChart contestGap={report.contest_practice_gap} />

              <RatingChart history={ratingHistory} loading={ratingLoading} />
              {ratingError && !ratingLoading && (
                <p className="error section-error">✗ {ratingError}</p>
              )}

              <RecommendationsList
                recommendations={recommendations}
                loading={recLoading}
              />
              {recError && !recLoading && (
                <p className="error section-error">✗ {recError}</p>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
