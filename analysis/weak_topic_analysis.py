from analysis.topic_analysis import analyze_topic_performance


def classify_topics(topic_stats: dict):
    """
    Classify topics into strong, medium, and weak based on success rate.
    """
    result = {
        "strong": {},
        "medium": {},
        "weak": {}
    }

    for topic, stats in topic_stats.items():
        attempted = stats["attempted"]
        solved = stats["solved"]

        if attempted == 0:
            continue

        success_rate = solved / attempted
        stats["success_rate"] = round(success_rate, 2)

        if success_rate >= 0.6:
            result["strong"][topic] = stats
        elif success_rate >= 0.4:
            result["medium"][topic] = stats
        else:
            result["weak"][topic] = stats

    return result


