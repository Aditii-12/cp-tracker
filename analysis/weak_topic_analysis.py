from analysis.topic_analysis import analyze_topic_performance


def get_weak_topics(handle: str, threshold: float = 0.5):
    """
    Identify weak topics based on success rate.
    """
    topic_stats = analyze_topic_performance(handle)

    weak_topics = {}
    for topic, stats in topic_stats.items():
        attempted = stats["attempted"]
        solved = stats["solved"]

        if attempted == 0:
            continue

        success_rate = solved / attempted

        if success_rate < threshold:
            weak_topics[topic] = {
                "attempted": attempted,
                "solved": solved,
                "failed": attempted - solved,
                "success_rate": round(success_rate, 2),
            }

    return weak_topics
