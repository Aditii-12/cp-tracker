from analysis.topic_analysis import analyze_topic_performance
from analysis.weak_topic_analysis import classify_topics
from analysis.difficulty_analysis import analyze_difficulty_performance
from analysis.contest_practice_gap import analyze_contest_practice_gap


def generate_full_report(handle: str, limit: int = 1000):
    """
    Generate a unified analytics report for a Codeforces user.

    Returns a dictionary containing:
    - topic_stats
    - topic_classification
    - difficulty_stats
    - contest_practice_gap
    """
    topic_stats = analyze_topic_performance(handle, limit)
    topic_classification = classify_topics(topic_stats)
    difficulty_stats = analyze_difficulty_performance(handle, limit)
    contest_gap = analyze_contest_practice_gap(handle, limit)

    report = {
        "handle": handle,
        "summary": {
            "total_topics": len(topic_stats),
            "weak_topics": len(topic_classification["weak"]),
            "strong_topics": len(topic_classification["strong"])
        },
        "topic_stats": topic_stats,
        "topic_classification": topic_classification,
        "difficulty_stats": difficulty_stats,
        "contest_practice_gap": contest_gap
    }

    return report



