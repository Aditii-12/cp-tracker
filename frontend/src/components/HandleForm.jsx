import { useState } from "react";

export default function HandleForm({ onSubmit, loading }) {
  const [handle, setHandle] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (handle.trim()) onSubmit(handle.trim());
  };

  return (
    <form onSubmit={handleSubmit} className="handle-form">
      <input
        type="text"
        placeholder="Enter Codeforces handle (e.g. tourist)"
        value={handle}
        onChange={(e) => setHandle(e.target.value)}
      />
      <button type="submit" disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </form>
  );
}
