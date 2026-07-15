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

    // Load secondary sections independently so one slow/failed
    // call doesn't block the rest of the dashboard.
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
      <h1>CP Tracker</h1>
      <HandleForm onSubmit={handleAnalyze} loading={loading} />

      {error && <p className="error">{error}</p>}

      {loading && (
        <div className="report-grid">
          <div className="chart-card">
            <h3>Topic Performance</h3>
            <div className="skeleton skeleton-chart" />
          </div>
          <div className="chart-card">
            <h3>Weak Topics</h3>
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
            <p className="error section-error">{ratingError}</p>
          )}

          <RecommendationsList
            recommendations={recommendations}
            loading={recLoading}
          />
          {recError && !recLoading && (
            <p className="error section-error">{recError}</p>
          )}
        </div>
      )}
    </div>
  );
}
