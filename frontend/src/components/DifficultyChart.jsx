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
      <h3>Difficulty Breakdown</h3>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="range" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="solved" fill="#60a5fa" />
          <Bar dataKey="failed" fill="#f87171" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
