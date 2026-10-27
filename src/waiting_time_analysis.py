
from collections import defaultdict
from datetime import datetime


def analyze_waiting_times(events):
    """Calculate time gaps between consecutive case activities."""
    grouped = defaultdict(list)
    results = []

    for event in events:
        case_id = str(event.get("case_id", "")).strip()
        activity = str(event.get("activity", "")).strip()
        timestamp = event.get("timestamp", "")

        if not case_id or not activity:
            continue

        try:
            parsed_time = datetime.strptime(
                timestamp, "%Y-%m-%d %H:%M:%S"
            )
        except (ValueError, TypeError):
            continue

        grouped[case_id].append((parsed_time, activity))

    for case_id, records in grouped.items():
        records.sort(key=lambda item: item[0])

        for index in range(1, len(records)):
            previous_time, previous_activity = records[index - 1]
            current_time, current_activity = records[index]

            waiting_minutes = (
                current_time - previous_time
            ).total_seconds() / 60

            results.append({
                "case_id": case_id,
                "from_activity": previous_activity,
                "to_activity": current_activity,
                "waiting_minutes": round(waiting_minutes, 2)
            })

    return results
  
