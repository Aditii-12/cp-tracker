from analysis.topic_analysis import analyze_topic_performance


def classify_topics(topic_stats: dict):
    """
    Classify topics into strong, medium, and weak categories
    based on success rate.

    Args:
        topic_stats (dict): Dictionary where each key is a topic name
                            and value contains 'attempted' and 'solved' counts.

    Returns:
        dict: Dictionary with three categories:
              - strong  : success_rate >= 0.60
              - medium  : 0.40 <= success_rate < 0.60
              - weak    : success_rate < 0.40
    """

    # Result container for classified topics
    result = {
        "strong": {},
        "medium": {},
        "weak": {}
    }

    # Iterate over each topic and its statistics
    for topic, stats in topic_stats.items():
        attempted = stats["attempted"]
        solved = stats["solved"]

        # Skip topics that were never attempted
        # (prevents division by zero)
        if attempted == 0:
            continue

        # Calculate success rate for the topic
        success_rate = solved / attempted

        # Store rounded success rate for reporting
        stats["success_rate"] = round(success_rate, 2)

        # Classify topic based on success rate thresholds
        if success_rate >= 0.6:
            result["strong"][topic] = stats
        elif success_rate >= 0.4:
            result["medium"][topic] = stats
        else:
            result["weak"][topic] = stats

    return result
