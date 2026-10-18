from collections import Counter
from datetime import datetime


def calculate_dashboard_metrics(events):
    """Calculate summary metrics from clinical event records."""
    valid_events = []
    cases = {}

    for event in events:
        case_id = event.get("case_id", "").strip()
        activity = event.get("activity", "").strip()

        try:
            timestamp = datetime.strptime(
                event.get("timestamp", "").strip(),
                "%Y-%m-%d %H:%M:%S"
            )
        except ValueError:
            continue

        if not case_id or not activity:
            continue

        valid_events.append({
            "case_id": case_id,
            "activity": activity,
            "timestamp": timestamp
        })

        cases.setdefault(case_id, []).append(timestamp)

    activity_counts = Counter(
        event["activity"] for event in valid_events
    )

    durations = []

    for timestamps in cases.values():
        timestamps.sort()
        seconds = (timestamps[-1] - timestamps[0]).total_seconds()
        durations.append(seconds)

    average_duration = (
        sum(durations) / len(durations) if durations else None
    )

    return {
        "total_cases": len(cases),
        "total_events": len(valid_events),
        "distinct_activities": len(activity_counts),
        "activity_frequency": dict(activity_counts),
        "average_case_duration_seconds": (
            round(average_duration, 2)
            if average_duration is not None else None
        )
    }


if __name__ == "__main__":
    print("CareFlow dashboard metrics module is ready.")
    print("Call calculate_dashboard_metrics(events) to calculate metrics.")
