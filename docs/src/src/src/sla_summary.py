def summarize_sla_breaches(breaches):
    activity_counts = {}
    total_excess_minutes = 0.0

    for breach in breaches:
        activity = breach["activity"]

        activity_counts[activity] = (
            activity_counts.get(activity, 0) + 1
        )
        total_excess_minutes += breach["breach_minutes"]

    return {
        "total_breaches": len(breaches),
        "affected_cases": len({
            breach["case_id"] for breach in breaches
        }),
        "activity_breach_counts": activity_counts,
        "total_excess_minutes": round(total_excess_minutes, 2)
    }
