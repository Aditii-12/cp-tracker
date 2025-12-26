from collections import defaultdict
from api.codeforces import get_user_submissions


def get_difficulty_bucket(rating: int):
    """
    Map problem rating to difficulty bucket.
    """
    if rating is None:
        return None

    if 800 <= rating <= 900:
        return "800-900"
    if 1000 <= rating <= 1100:
        return "1000-1100"

    return None


def analyze_difficulty_performance(handle: str, limit: int = 1000):
    """
    Analyze performance based on problem difficulty buckets.

    Returns:
    {
        bucket: {
            "attempted": int,
            "solved": int,
            "failed": int,
            "success_rate": float
        }
    }
    """
    submissions = get_user_submissions(handle, limit)

    diff_stats = defaultdict(lambda: {
        "attempted": 0,
        "solved": 0,
        "failed": 0
    })

    for sub in submissions:
        problem = sub.get("problem", {})
        rating = problem.get("rating")
        verdict = sub.get("verdict")

        bucket = get_difficulty_bucket(rating)
        if bucket is None:
            continue

        diff_stats[bucket]["attempted"] += 1

        if verdict == "OK":
            diff_stats[bucket]["solved"] += 1
        else:
            diff_stats[bucket]["failed"] += 1

    # compute success rate
    for bucket, stats in diff_stats.items():
        attempted = stats["attempted"]
        stats["success_rate"] = round(stats["solved"] / attempted, 2) if attempted > 0 else 0.0

    return dict(diff_stats)


