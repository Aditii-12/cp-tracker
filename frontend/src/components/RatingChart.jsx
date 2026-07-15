import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid,
} from "recharts";
import { ratingColor, ratingTier } from "../utils/ratingColor";

export default function RatingChart({ history, loading }) {
  if (loading) {
    return (
      <div className="chart-card">
        <h3>rating progression</h3>
        <div className="skeleton skeleton-chart" />
      </div>
    );
  }

  if (!history || history.length === 0) {
    return (
      <div className="chart-card">
        <h3>rating progression</h3>
        <p>No contest history found for this user.</p>
      </div>
    );
  }

  const data = history.map((h) => ({
    ...h,
    date: new Date(h.date * 1000).toLocaleDateString(),
  }));

  const peak = Math.max(...data.map((h) => h.rating));
  const current = data[data.length - 1].rating;
  const biggestDrop = Math.min(...data.map((h) => h.change));
  const lineColor = ratingColor(current);

  return (
    <div className="chart-card">
      <h3>rating progression</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" stroke="#232935" />
          <XAxis dataKey="date" tick={{ fill: "#8b95a5", fontSize: 11 }} stroke="#4d5666" />
          <YAxis
            domain={["dataMin - 100", "dataMax + 100"]}
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
          <Line
            type="monotone"
            dataKey="rating"
            stroke={lineColor}
            strokeWidth={2}
            dot={{ r: 3, fill: lineColor }}
          />
        </LineChart>
      </ResponsiveContainer>
      <p className="rating-summary">
        <span className="rating-chip" style={{ background: lineColor }} />
        current: <strong style={{ color: lineColor }}>{current}</strong> ({ratingTier(current)}) ·
        peak: <strong>{peak}</strong> · contests: <strong>{data.length}</strong> · biggest drop:{" "}
        <strong style={{ color: biggestDrop < 0 ? "#e5484d" : "#2ea043" }}>
          {biggestDrop}
        </strong>
      </p>
    </div>
  );
}
