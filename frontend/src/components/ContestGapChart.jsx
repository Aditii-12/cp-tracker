export default function ContestGapChart({ contestGap }) {
  const entries = Object.entries(contestGap || {}).sort(
    (a, b) => b[1].gap - a[1].gap
  );

  return (
    <div className="chart-card">
      <h3>Contest vs Practice Gap</h3>
      <table>
        <thead>
          <tr>
            <th>Topic</th>
            <th>Contest Success</th>
            <th>Practice Success</th>
            <th>Gap</th>
          </tr>
        </thead>
        <tbody>
          {entries.map(([topic, stats]) => (
            <tr key={topic}>
              <td>{topic}</td>
              <td>{(stats.contest_success_rate * 100).toFixed(0)}%</td>
              <td>{(stats.practice_success_rate * 100).toFixed(0)}%</td>
              <td style={{ color: stats.gap > 0 ? "#f87171" : "#4ade80" }}>
                {(stats.gap * 100).toFixed(0)}%
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
