import { useState } from "react";

export default function HandleForm({ onSubmit, loading }) {
  const [handle, setHandle] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (handle.trim()) onSubmit(handle.trim());
  };

  return (
    <form onSubmit={handleSubmit} className="handle-form">
      <span className="prompt-glyph">cf analyze</span>
      <input
        type="text"
        placeholder="handle (e.g. tourist)"
        value={handle}
        onChange={(e) => setHandle(e.target.value)}
        autoFocus
      />
      <button type="submit" disabled={loading}>
        {loading ? "running..." : "run →"}
      </button>
    </form>
  );
}
