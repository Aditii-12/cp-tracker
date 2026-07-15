import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";

export default function RatingChart({ history, loading }) {
  if (loading) {
    return (
      <div className="chart-card">
        <h3>Rating Progression</h3>
        <div className="skeleton skeleton-chart" />
      </div>
    );
  }

  if (!history || history.length === 0) {
    return (
      <div className="chart-card">
        <h3>Rating Progression</h3>
        <p>No contest history found for this user.</p>
      </div>
    );
  }

  const data = history.map((h) => ({
    ...h,
    date: new Date(h.date * 1000).toLocaleDateString(),
  }));

  const peak = Math.max(...data.map((h) => h.rating));
  const biggestDrop = Math.min(...data.map((h) => h.change));

  return (
    <div className="chart-card">
      <h3>Rating Progression</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="date" tick={{ fontSize: 11 }} />
          <YAxis domain={["dataMin - 100", "dataMax + 100"]} />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="rating"
            stroke="#4ade80"
            dot={{ r: 3 }}
          />
        </LineChart>
      </ResponsiveContainer>
      <p className="rating-summary">
        Peak rating: <strong>{peak}</strong> · Contests: <strong>{data.length}</strong> · Biggest drop:{" "}
        <strong style={{ color: biggestDrop < 0 ? "#f87171" : "#4ade80" }}>
          {biggestDrop}
        </strong>
      </p>
    </div>
  );
}
