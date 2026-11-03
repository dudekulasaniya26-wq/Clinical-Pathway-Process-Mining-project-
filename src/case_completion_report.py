REQUIRED_ACTIVITIES = [
    "Registration",
    "Doctor Consultation",
    "Lab Test",
    "Treatment",
    "Discharge"
]


def generate_case_completion_report(events):
    case_ids = sorted({
        event["case_id"] for event in events
    })

    reports = []

    for case_id in case_ids:
        completed = {
            event["activity"]
            for event in events
            if event["case_id"] == case_id
        }

        pending = [
            activity
            for activity in REQUIRED_ACTIVITIES
            if activity not in completed
        ]

        reports.append({
            "case_id": case_id,
            "completed_activities": sorted(completed),
            "pending_activities": pending,
            "status": (
                "Completed" if not pending
                else "Pending"
            )
        })

    return reports
