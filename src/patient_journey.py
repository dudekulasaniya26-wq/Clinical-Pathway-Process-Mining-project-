
from datetime import datetime

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def build_patient_journey(events, case_id):
    """Build a chronological timeline for one case."""
    journey = []

    for event in events:
        if str(event.get("case_id", "")).strip() != str(case_id):
            continue

        try:
            timestamp = datetime.strptime(
                event.get("timestamp", ""), TIMESTAMP_FORMAT
            )
        except (ValueError, TypeError):
            continue

        activity = str(event.get("activity", "")).strip()
        if not activity:
            continue

        journey.append({
            "activity": activity,
            "timestamp": timestamp
        })

    journey.sort(key=lambda item: item["timestamp"])

    result = []
    previous_time = None

    for item in journey:
        elapsed = (
            (item["timestamp"] - previous_time).total_seconds()
            if previous_time else None
        )

        result.append({
            "activity": item["activity"],
            "timestamp": item["timestamp"].strftime(TIMESTAMP_FORMAT),
            "elapsed_seconds": elapsed
        })

        previous_time = item["timestamp"]

    return result
    
