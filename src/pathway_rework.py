from collections import defaultdict
from datetime import datetime


def analyze_pathway_rework(events):
    """Identify repeated activities within each clinical case."""
    grouped = defaultdict(list)

    for event in events:
        case_id = str(event.get("case_id", "")).strip()
        activity = str(event.get("activity", "")).strip()
        timestamp = event.get("timestamp", "")

        if case_id and activity:
            grouped[case_id].append({
                "activity": activity,
                "timestamp": timestamp
            })

    results = []

    for case_id, records in grouped.items():
        records.sort(
            key=lambda item: item["timestamp"]
        )

        seen = set()
        repeated = []

        for record in records:
            activity = record["activity"]

            if activity in seen and activity not in repeated:
                repeated.append(activity)

            seen.add(activity)

        results.append({
            "case_id": case_id,
            "rework_detected": bool(repeated),
            "repeated_activities": repeated,
            "rework_activity_count": len(repeated)
        })

    return results
