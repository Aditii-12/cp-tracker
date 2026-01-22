from analysis.topic_analysis import analyze_topic_performance
from analysis.weak_topic_analysis import get_weak_topics
from analysis.difficulty_analysis import analyze_difficulty_performance


def generate_full_report(handle: str):
    return {
        "topic_analysis": analyze_topic_performance(handle),
        "weak_topics": get_weak_topics(handle),
        "difficulty_analysis": analyze_difficulty_performance(handle),
    }


if __name__ == "__main__":
    HANDLE = "tourist"
    report = generate_full_report(HANDLE)

    print("\n=== TOPIC ANALYSIS ===")
    print(report["topic_analysis"])

    print("\n=== WEAK TOPICS ===")
    print(report["weak_topics"])

    print("\n=== DIFFICULTY ANALYSIS ===")
    print(report["difficulty_analysis"])
