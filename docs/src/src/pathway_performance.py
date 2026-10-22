from datetime import datetime

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"


def calculate_pathway_performance(pathways, events):
    """Calculate duration statistics for each pathway variant."""
    case_events = {}

    for event in events:
        case_id = str(event.get("case_id", "")).strip()

        if not case_id:
            continue

        try:
            timestamp = datetime.strptime(
                event.get("timestamp", ""), TIMESTAMP_FORMAT
            )
        except (ValueError, TypeError):
            continue

        case_events.setdefault(case_id, []).append(timestamp)

    results = []

    for pathway in pathways:
        durations = []

        for case_id in pathway.get("case_ids", []):
            timestamps = case_events.get(case_id, [])

            if timestamps:
                duration = (
                    max(timestamps) - min(timestamps)
                ).total_seconds()
                durations.append(duration)

        results.append({
            "variant_id": pathway.get("variant_id"),
            "case_count": pathway.get("case_count", 0),
            "activity_count": len(pathway.get("activities", [])),
            "average_duration_seconds": round(
                sum(durations) / len(durations), 2
            ) if durations else None,
            "minimum_duration_seconds": min(durations)
            if durations else None,
            "maximum_duration_seconds": max(durations)
            if durations else None
        })

    return results
