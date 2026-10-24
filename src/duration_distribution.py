
from datetime import datetime
from statistics import mean, median


def analyze_case_durations(events):
    case_times = {}

    for event in events:
        case_id = str(event.get("case_id", "")).strip()

        if not case_id:
            continue

        try:
            timestamp = datetime.strptime(
                event["timestamp"], "%Y-%m-%d %H:%M:%S"
            )
        except (KeyError, ValueError, TypeError):
            continue

        case_times.setdefault(case_id, []).append(timestamp)

    durations = []

    for case_id, timestamps in case_times.items():
        duration = (
            max(timestamps) - min(timestamps)
        ).total_seconds() / 60

        durations.append({
            "case_id": case_id,
            "duration_minutes": round(duration, 2)
        })

    values = [item["duration_minutes"] for item in durations]

    return {
        "case_durations": durations,
        "case_count": len(values),
        "average_minutes": round(mean(values), 2) if values else 0,
        "median_minutes": round(median(values), 2) if values else 0,
        "shortest_minutes": min(values) if values else 0,
        "longest_minutes": max(values) if values else 0
      }
  
