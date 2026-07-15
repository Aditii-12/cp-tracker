export default function RecommendationsList({ recommendations, loading }) {
  if (loading) {
    return (
      <div className="chart-card">
        <h3>Recommended Problems</h3>
        <div className="skeleton skeleton-list" />
      </div>
    );
  }

  const entries = Object.entries(recommendations || {});

  if (entries.length === 0) {
    return (
      <div className="chart-card">
        <h3>Recommended Problems</h3>
        <p>No recommendations available — solid across all weak topics!</p>
      </div>
    );
  }

  return (
    <div className="chart-card">
      <h3>Recommended Problems</h3>
      {entries.map(([topic, problems]) => (
        <div key={topic} className="rec-group">
          <h4>{topic}</h4>
          <ul className="rec-list">
            {problems.map((p) => (
              <li key={p.url}>
                <a href={p.url} target="_blank" rel="noopener noreferrer">
                  {p.name}
                </a>
                <span className="rec-rating">{p.rating}</span>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}
