from collections import defaultdict
from api.codeforces import get_user_submissions


def get_difficulty_bucket(rating: int):
    """
    Map a problem rating to a predefined difficulty bucket.

    Args:
        rating (int): Codeforces problem rating.

    Returns:
        str | None: Difficulty bucket label (e.g. '800-900', '1000-1100')
                    or None if rating does not fall in tracked ranges.
    """
    # Rating can be missing for some problems
    if rating is None:
        return None

    # Beginner-level problems
    if 800 <= rating <= 900:
        return "800-900"

    # Lower-medium difficulty problems
    if 1000 <= rating <= 1100:
        return "1000-1100"

    # Ignore ratings outside tracked buckets
    return None


def analyze_difficulty_performance(handle: str, limit: int = 1000):
    """
    Analyze user performance based on problem difficulty buckets.

    Fetches recent submissions for a user and aggregates statistics
    such as attempted, solved, failed, and success rate per bucket.

    Args:
        handle (str): Codeforces user handle.
        limit (int): Maximum number of submissions to analyze.

    Returns:
        dict: Mapping of difficulty bucket to performance stats:
              {
                  bucket: {
                      "attempted": int,
                      "solved": int,
                      "failed": int,
                      "success_rate": float
                  }
              }
    """
    # Fetch recent submissions from Codeforces API
    submissions = get_user_submissions(handle, limit)

    # Initialize statistics container for each difficulty bucket
    diff_stats = defaultdict(lambda: {
        "attempted": 0,
        "solved": 0,
        "failed": 0
    })

    # Process each submission
    for sub in submissions:
        problem = sub.get("problem", {})
        rating = problem.get("rating")
        verdict = sub.get("verdict")

        # Determine which difficulty bucket this problem belongs to
        bucket = get_difficulty_bucket(rating)
        if bucket is None:
            continue

        # Count this submission as an attempt
        diff_stats[bucket]["attempted"] += 1

        # Update solved / failed counts based on verdict
        if verdict == "OK":
            diff_stats[bucket]["solved"] += 1
        else:
            diff_stats[bucket]["failed"] += 1

    # Compute success rate for each difficulty bucket
    for bucket, stats in diff_stats.items():
        attempted = stats["attempted"]
        stats["success_rate"] = (
            round(stats["solved"] / attempted, 2) if attempted > 0 else 0.0
        )

    return dict(diff_stats)
