// Codeforces' own rank-color convention. Used consistently across the
// dashboard so a rating always reads the same way it would on CF itself.
export function ratingColor(rating) {
  if (rating == null) return "#6b7280";
  if (rating < 1200) return "#6b7280"; // gray — newbie
  if (rating < 1400) return "#1cba52"; // green — pupil
  if (rating < 1600) return "#17b6cf"; // cyan — specialist
  if (rating < 1900) return "#3b6fd6"; // blue — expert
  if (rating < 2100) return "#a34cd1"; // purple — candidate master
  if (rating < 2400) return "#e8951b"; // orange — master
  return "#e5484d"; // red — grandmaster+
}

export function ratingTier(rating) {
  if (rating == null) return "unrated";
  if (rating < 1200) return "newbie";
  if (rating < 1400) return "pupil";
  if (rating < 1600) return "specialist";
  if (rating < 1900) return "expert";
  if (rating < 2100) return "candidate master";
  if (rating < 2400) return "master";
  return "grandmaster";
}
