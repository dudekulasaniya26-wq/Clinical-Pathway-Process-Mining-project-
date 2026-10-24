from collections import Counter


def rank_activities(events):
    counts = Counter()

    for event in events:
        activity = str(event.get("activity", "")).strip()

        if activity:
            counts[activity] += 1

    ranked = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0].lower())
    )

    return [
        {
            "rank": index,
            "activity": activity,
            "event_count": count
        }
        for index, (activity, count) in enumerate(ranked, start=1)
    ]
