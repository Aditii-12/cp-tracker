from analysis.topic_analysis import analyze_topic_performance
from analysis.weak_topic_analysis import classify_topics
from analysis.difficulty_analysis import analyze_difficulty_performance

HANDLE = "dhruv83170"
LIMIT = 700

print("\n=== TOPIC ANALYSIS ===")
topic_stats = analyze_topic_performance(HANDLE, LIMIT)
for t, d in list(topic_stats.items())[:5]:
    print(t, d)

print("\n=== WEAK TOPICS ===")
classified = classify_topics(topic_stats)
for t, d in classified["weak"].items():
    print(t, d)

print("\n=== DIFFICULTY ANALYSIS ===")
diff_stats = analyze_difficulty_performance(HANDLE, LIMIT)
for b, d in diff_stats.items():
    print(b, d)
