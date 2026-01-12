from collections import defaultdict
from api.codeforces import get_user_submissions


def analyze_contest_practice_gap(handle: str, limit: int = 1000):
    """
    Analyze topic-wise performance gap between contest and practice.

    Returns:
    {
        topic: {
            "contest_attempted": int,
            "contest_solved": int,
            "practice_attempted": int,
            "practice_solved": int,
            "contest_success_rate": float,
            "practice_success_rate": float,
            "gap": float
        }
    }
    """
    submissions = get_user_submissions(handle, limit)

    stats = defaultdict(lambda: {
        "contest_attempted": 0,
        "contest_solved": 0,
        "practice_attempted": 0,
        "practice_solved": 0
    })

    for sub in submissions:
        problem = sub.get("problem", {})
        tags = problem.get("tags", [])
        verdict = sub.get("verdict")
        participant_type = sub.get("author", {}).get("participantType")

        if not tags:
            continue

        is_contest = participant_type == "CONTESTANT"

        for tag in tags:
            if is_contest:
                stats[tag]["contest_attempted"] += 1
                if verdict == "OK":
                    stats[tag]["contest_solved"] += 1
            else:
                stats[tag]["practice_attempted"] += 1
                if verdict == "OK":
                    stats[tag]["practice_solved"] += 1

    # compute success rates and gap
    result = {}
    for topic, s in stats.items():
        ca = s["contest_attempted"]
        pa = s["practice_attempted"]

        contest_sr = (s["contest_solved"] / ca) if ca > 0 else 0.0
        practice_sr = (s["practice_solved"] / pa) if pa > 0 else 0.0

        result[topic] = {
            **s,
            "contest_success_rate": round(contest_sr, 2),
            "practice_success_rate": round(practice_sr, 2),
            "gap": round(practice_sr - contest_sr, 2)
        }

    return result


# # ---- TEMP TEST ----
# if __name__ == "__main__":
#     gap_stats = analyze_contest_practice_gap("aditisahu12", 1000)

#     print("Topics with largest negative contest gap:")
#     for t, d in sorted(gap_stats.items(), key=lambda x: x[1]["gap"])[:5]:
#         print(t, d)
