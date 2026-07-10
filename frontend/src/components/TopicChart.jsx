import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

export default function TopicChart({ topicAnalysis }) {
  const data = Object.entries(topicAnalysis || {})
    .map(([topic, stats]) => ({
      topic,
      solved: stats.solved,
      failed: stats.failed,
    }))
    .sort((a, b) => b.solved - a.solved)
    .slice(0, 15);

  return (
    <div className="chart-card">
      <h3>Topic Performance (Top 15)</h3>
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data} layout="vertical" margin={{ left: 100 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis type="number" />
          <YAxis type="category" dataKey="topic" width={140} />
          <Tooltip />
          <Bar dataKey="solved" fill="#4ade80" stackId="a" />
          <Bar dataKey="failed" fill="#f87171" stackId="a" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
