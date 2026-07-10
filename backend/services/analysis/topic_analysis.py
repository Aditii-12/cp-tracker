from collections import defaultdict
from api.codeforces import get_user_submissions


def analyze_topic_performance(handle: str, limit: int = 1000):
    """
    Analyze topic-wise performance from user submissions.

    Returns a dictionary of the form:
    {
        topic: {
            "attempted": int,
            "solved": int,
            "failed": int
        }
    }
    """
    submissions = get_user_submissions(handle, limit)

    topic_stats = defaultdict(lambda: {
        "attempted": 0,
        "solved": 0,
        "failed": 0
    })

    for sub in submissions:
        problem = sub.get("problem", {})
        tags = problem.get("tags", [])

        if not tags:
            continue

        verdict = sub.get("verdict")

        for tag in tags:
            topic_stats[tag]["attempted"] += 1

            if verdict == "OK":
                topic_stats[tag]["solved"] += 1
            else:
                topic_stats[tag]["failed"] += 1

    return dict(topic_stats)



