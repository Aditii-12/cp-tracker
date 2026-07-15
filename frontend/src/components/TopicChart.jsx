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
      <h3>topic performance (top 15)</h3>
      <ResponsiveContainer width="100%" height={400}>
        <BarChart data={data} layout="vertical" margin={{ left: 100 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#232935" />
          <XAxis type="number" stroke="#4d5666" tick={{ fill: "#8b95a5", fontSize: 12 }} />
          <YAxis
            type="category"
            dataKey="topic"
            width={140}
            stroke="#4d5666"
            tick={{ fill: "#8b95a5", fontSize: 12 }}
          />
          <Tooltip
            contentStyle={{
              background: "#171c25",
              border: "1px solid #232935",
              borderRadius: 8,
              fontSize: 13,
            }}
            labelStyle={{ color: "#e3e8ef" }}
          />
          <Bar dataKey="solved" fill="#2ea043" stackId="a" radius={[0, 0, 0, 0]} />
          <Bar dataKey="failed" fill="#e5484d" stackId="a" radius={[0, 3, 3, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
