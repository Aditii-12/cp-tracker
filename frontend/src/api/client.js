import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function fetchAnalysis(handle) {
  const res = await axios.get(`${API_BASE}/analyze/${handle}`);
  return res.data;
}
