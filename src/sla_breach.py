
from datetime import datetime


def detect_sla_breaches(events, sla_limits):
    """
    Detect activities that exceed their allowed duration.

    events: list of event dictionaries containing
            case_id, activity, timestamp
    sla_limits: dictionary mapping activity to allowed minutes
    """
    grouped = {}

    for event in events:
        try:
            timestamp = datetime.strptime(
                event["timestamp"], "%Y-%m-%d %H:%M:%S"
            )
        except (KeyError, ValueError, TypeError):
            continue

        case_id = event.get("case_id", "").strip()
        activity = event.get("activity", "").strip()

        if not case_id or not activity:
            continue

        grouped.setdefault(case_id, []).append(
            (timestamp, activity)
        )

    breaches = []

    for case_id, records in grouped.items():
        records.sort(key=lambda item: item[0])

        for index in range(len(records) - 1):
            start_time, activity = records[index]
            next_time, _ = records[index + 1]

            if activity not in sla_limits:
                continue

            elapsed_minutes = (
                next_time - start_time
            ).total_seconds() / 60

            allowed_minutes = sla_limits[activity]

            if elapsed_minutes > allowed_minutes:
                breaches.append({
                    "case_id": case_id,
                    "activity": activity,
                    "elapsed_minutes": round(elapsed_minutes, 2),
                    "allowed_minutes": allowed_minutes,
                    "breach_minutes": round(
                        elapsed_minutes - allowed_minutes, 2
                    )
                })

    return breaches
      
