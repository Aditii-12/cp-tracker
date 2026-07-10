import { useState } from "react";
import { fetchAnalysis } from "../api/client";
import HandleForm from "../components/HandleForm";
import TopicChart from "../components/TopicChart";
import WeakTopicsList from "../components/WeakTopicsList";
import DifficultyChart from "../components/DifficultyChart";
import ContestGapChart from "../components/ContestGapChart";

export default function Dashboard() {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAnalyze = async (handle) => {
    setLoading(true);
    setError(null);
    setReport(null);
    try {
      const data = await fetchAnalysis(handle);
      setReport(data);
    } catch (err) {
      setError(
        err.response?.data?.detail || "Something went wrong. Check the handle."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="dashboard">
      <h1>CP Tracker</h1>
      <HandleForm onSubmit={handleAnalyze} loading={loading} />

      {error && <p className="error">{error}</p>}

      {report && (
        <div className="report-grid">
          <TopicChart topicAnalysis={report.topic_analysis} />
          <WeakTopicsList weakTopics={report.weak_topics} />
          <DifficultyChart difficultyAnalysis={report.difficulty_analysis} />
          <ContestGapChart contestGap={report.contest_practice_gap} />
        </div>
      )}
    </div>
  );
}
