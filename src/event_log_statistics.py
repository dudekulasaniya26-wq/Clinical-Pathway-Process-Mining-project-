
from collections import Counter


def calculate_event_log_statistics(events):
    """Calculate basic statistics for a clinical event log."""
    if not events:
        return {
            "total_events": 0,
            "unique_cases": 0,
            "unique_activities": 0,
            "events_per_case": {}
        }

    case_ids = {
        str(event.get("case_id", "")).strip()
        for event in events
        if str(event.get("case_id", "")).strip()
    }

    activities = {
        str(event.get("activity", "")).strip()
        for event in events
        if str(event.get("activity", "")).strip()
    }

    counts = Counter(
        str(event.get("case_id", "")).strip()
        for event in events
        if str(event.get("case_id", "")).strip()
    )

    return {
        "total_events": len(events),
        "unique_cases": len(case_ids),
        "unique_activities": len(activities),
        "events_per_case": dict(counts)
  }
  
