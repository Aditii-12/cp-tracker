import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

export default function DifficultyChart({ difficultyAnalysis }) {
  const data = Object.entries(difficultyAnalysis || {}).map(
    ([range, stats]) => ({
      range,
      solved: stats.solved,
      failed: stats.failed,
    })
  );

  return (
    <div className="chart-card">
      <h3>difficulty breakdown</h3>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#232935" />
          <XAxis dataKey="range" stroke="#4d5666" tick={{ fill: "#8b95a5", fontSize: 12 }} />
          <YAxis stroke="#4d5666" tick={{ fill: "#8b95a5", fontSize: 12 }} />
          <Tooltip
            contentStyle={{
              background: "#171c25",
              border: "1px solid #232935",
              borderRadius: 8,
              fontSize: 13,
            }}
            labelStyle={{ color: "#e3e8ef" }}
          />
          <Bar dataKey="solved" fill="#3b6fd6" radius={[3, 3, 0, 0]} />
          <Bar dataKey="failed" fill="#e5484d" radius={[3, 3, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
