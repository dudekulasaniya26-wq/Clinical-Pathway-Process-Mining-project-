from collections import defaultdict
from datetime import datetime


def detect_unusual_sequences(events, allowed_transitions):
    """Find transitions not included in the allowed transition list."""
    grouped = defaultdict(list)

    for event in events:
        case_id = str(event.get("case_id", "")).strip()
        activity = str(event.get("activity", "")).strip()

        try:
            timestamp = datetime.strptime(
                event.get("timestamp", ""),
                "%Y-%m-%d %H:%M:%S"
            )
        except (ValueError, TypeError):
            continue

        if case_id and activity:
            grouped[case_id].append((timestamp, activity))

    allowed = set(allowed_transitions)
    results = []

    for case_id, records in grouped.items():
        records.sort(key=lambda item: item[0])
        activities = [activity for _, activity in records]
        unusual = []

        for index in range(len(activities) - 1):
            transition = (
                activities[index],
                activities[index + 1]
            )

            if transition not in allowed:
                unusual.append({
                    "from_activity": transition[0],
                    "to_activity": transition[1]
                })

        results.append({
            "case_id": case_id,
            "unusual_transitions": unusual,
            "unusual_count": len(unusual)
        })

    return results
