export default function WeakTopicsList({ weakTopics }) {
  const entries = Object.entries(weakTopics || {}).sort(
    (a, b) => a[1].success_rate - b[1].success_rate
  );

  if (entries.length === 0) {
    return (
      <div className="chart-card">
        <h3>Weak Topics</h3>
        <p>No weak topics found — nice work!</p>
      </div>
    );
  }

  return (
    <div className="chart-card">
      <h3>Weak Topics</h3>
      <table>
        <thead>
          <tr>
            <th>Topic</th>
            <th>Attempted</th>
            <th>Solved</th>
            <th>Success Rate</th>
          </tr>
        </thead>
        <tbody>
          {entries.map(([topic, stats]) => (
            <tr key={topic}>
              <td>{topic}</td>
              <td>{stats.attempted}</td>
              <td>{stats.solved}</td>
              <td>{(stats.success_rate * 100).toFixed(0)}%</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
