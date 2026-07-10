from analysis.topic_analysis import analyze_topic_performance
from analysis.weak_topic_analysis import get_weak_topics
from analysis.difficulty_analysis import analyze_difficulty_performance
from analysis.contest_practice_gap import analyze_contest_practice_gap



def generate_full_report(handle: str):
    return {
        "topic_analysis": analyze_topic_performance(handle),
        "weak_topics": get_weak_topics(handle),
        "difficulty_analysis": analyze_difficulty_performance(handle),
        "contest_practice_gap": analyze_contest_practice_gap(handle),
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

    print("\n=== CONTEST VS PRACTICE GAP ===")
    print(report["contest_practice_gap"])


