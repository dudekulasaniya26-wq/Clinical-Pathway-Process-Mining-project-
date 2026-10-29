
from collections import defaultdict


def detect_missing_activities(events, expected_activities):
    """Find expected activities missing from each case."""
    case_activities = defaultdict(set)

    for event in events:
        case_id = str(event.get("case_id", "")).strip()
        activity = str(event.get("activity", "")).strip()

        if case_id and activity:
            case_activities[case_id].add(activity)

    results = []

    for case_id, activities in case_activities.items():
        missing = [
            activity
            for activity in expected_activities
            if activity not in activities
        ]

        results.append({
            "case_id": case_id,
            "missing_activities": missing,
            "missing_count": len(missing)
        })

    return results
  
