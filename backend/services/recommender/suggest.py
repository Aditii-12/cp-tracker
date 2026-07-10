from backend.services.api.codeforces import get_problemset, get_user_info, get_submissions


def get_solved_set(submissions):
    solved = set()
    for s in submissions:
        if s["verdict"] == "OK":
            p = s["problem"]
            solved.add((p.get("contestId", 0), p["index"]))
    return solved


def recommend_problems(handle, weak_topics, count=5):
    if not weak_topics:
        return {}

    try:
        info = get_user_info(handle)
        user_rating = info.get("rating", 1200)
    except Exception:
        user_rating = 1200

    min_r = max(800, user_rating - 200)
    max_r = user_rating + 300

    try:
        submissions = get_submissions(handle)
        solved = get_solved_set(submissions)
    except Exception:
        solved = set()

    recommendations = {}

    for topic in list(weak_topics.keys())[:5]:
        try:
            problems = get_problemset(tags=[topic], min_rating=min_r, max_rating=max_r)
        except Exception:
            continue

        unsolved = [
            p for p in problems
            if (p.get("contestId", 0), p.get("index", "")) not in solved
            and p.get("rating")
        ]

        unsolved.sort(key=lambda p: p.get("rating", 0))
        picked = unsolved[:count]

        if picked:
            recommendations[topic] = [
                {
                    "name": p["name"],
                    "rating": p.get("rating", "N/A"),
                    "tags": p.get("tags", []),
                    "url": f"https://codeforces.com/problemset/problem/{p.get('contestId','')}/{p.get('index','')}"
                }
                for p in picked
            ]

    return recommendations