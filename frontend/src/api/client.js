import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function fetchAnalysis(handle) {
  const res = await axios.get(`${API_BASE}/analyze/${handle}`);
  return res.data;
}

export async function fetchRecommendations(handle) {
  const res = await axios.get(`${API_BASE}/analyze/${handle}/recommendations`);
  return res.data;
}

export async function fetchRatingHistory(handle) {
  const res = await axios.get(`${API_BASE}/analyze/${handle}/rating-history`);
  return res.data;
}
