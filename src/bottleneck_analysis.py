from collections import defaultdict
from datetime import datetime

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def detect_bottlenecks(events):
    """Rank activity transitions by average waiting time in seconds."""
    cases = defaultdict(list)

    for event in events:
        case_id = str(event.get("case_id", "")).strip()
        activity = str(event.get("activity", "")).strip()

        if not case_id or not activity:
            continue

        try:
            timestamp = datetime.strptime(
                event.get("timestamp", ""), TIMESTAMP_FORMAT
            )
        except (ValueError, TypeError):
            continue

        cases[case_id].append((timestamp, activity))

    waiting_times = defaultdict(list)

    for case_events in cases.values():
        case_events.sort(key=lambda item: item[0])

        for index in range(len(case_events) - 1):
            current_time, current_activity = case_events[index]
            next_time, next_activity = case_events[index + 1]

            seconds = (next_time - current_time).total_seconds()

            if seconds >= 0:
                transition = (current_activity, next_activity)
                waiting_times[transition].append(seconds)

    results = []

    for (source, target), values in waiting_times.items():
        results.append({
            "from_activity": source,
            "to_activity": target,
            "average_wait_seconds": round(sum(values) / len(values), 2),
            "observation_count": len(values)
        })

    return sorted(
        results,
        key=lambda item: item["average_wait_seconds"],
        reverse=True
  )
