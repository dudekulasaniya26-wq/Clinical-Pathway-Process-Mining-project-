MILESTONES = [
    "Registration",
    "Doctor Consultation",
    "Lab Test",
    "Treatment",
    "Discharge"
]


def track_case_milestones(events, case_id):
    case_events = [
        event for event in events
        if event.get("case_id") == case_id
    ]

    completed = {
        event["activity"] for event in case_events
    }

    result = []

    for milestone in MILESTONES:
        result.append({
            "milestone": milestone,
            "completed": milestone in completed
        })

    return result


def calculate_milestone_progress(events, case_id):
    result = track_case_milestones(events, case_id)

    total = len(result)
    completed = sum(
        1 for item in result if item["completed"]
    )

    percentage = (
        completed / total * 100 if total else 0
    )

    return {
        "case_id": case_id,
        "completed_milestones": completed,
        "total_milestones": total,
        "progress_percentage": round(percentage, 2),
        "milestones": result
    }
