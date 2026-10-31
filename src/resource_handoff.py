
from collections import defaultdict
from datetime import datetime


def detect_resource_handoffs(events):
    """Identify resource changes between consecutive activities."""
    grouped = defaultdict(list)

    for event in events:
        case_id = str(event.get("case_id", "")).strip()
        activity = str(event.get("activity", "")).strip()
        resource = str(event.get("resource", "")).strip()

        if not case_id or not activity or not resource:
            continue

        try:
            timestamp = datetime.strptime(
                event.get("timestamp", ""),
                "%Y-%m-%d %H:%M:%S"
            )
        except (ValueError, TypeError):
            continue

        grouped[case_id].append(
            (timestamp, activity, resource)
        )

    results = []

    for case_id, records in grouped.items():
        records.sort(key=lambda item: item[0])

        for index in range(1, len(records)):
            previous = records[index - 1]
            current = records[index]

            if previous[2] != current[2]:
                results.append({
                    "case_id": case_id,
                    "previous_activity": previous[1],
                    "previous_resource": previous[2],
                    "current_activity": current[1],
                    "current_resource": current[2],
                    "handoff_detected": True
                })

    return results
              
