def summarize_filter_results(original_events, filtered_events):
    def count_cases(events):
        return len({
            str(event.get("case_id", "")).strip()
            for event in events
            if str(event.get("case_id", "")).strip()
        })

    original_count = len(original_events)
    filtered_count = len(filtered_events)

    removed_count = max(0, original_count - filtered_count)

    if original_count:
        retained_percentage = round(
            filtered_count / original_count * 100, 2
        )
    else:
        retained_percentage = 0.0

    return {
        "original_events": original_count,
        "filtered_events": filtered_count,
        "removed_events": removed_count,
        "original_cases": count_cases(original_events),
        "filtered_cases": count_cases(filtered_events),
        "retained_percentage": retained_percentage
    }
