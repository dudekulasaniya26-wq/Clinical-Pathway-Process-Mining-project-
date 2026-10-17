from collections import Counter, defaultdict
from datetime import datetime


def discover_pathways(events):
    """Group cases by their ordered activity sequences."""
    cases = defaultdict(list)

    for event in events:
        case_id = event.get("case_id", "").strip()
        activity = event.get("activity", "").strip()
        timestamp = event.get("timestamp", "").strip()

        if not case_id or not activity:
            continue

        try:
            event_time = datetime.strptime(
                timestamp, "%Y-%m-%d %H:%M:%S"
            )
        except ValueError:
            continue

        cases[case_id].append((event_time, activity))

    variant_counts = Counter()
    variant_cases = defaultdict(list)

    for case_id, case_events in cases.items():
        case_events.sort(key=lambda item: item[0])
        sequence = tuple(activity for _, activity in case_events)

        variant_counts[sequence] += 1
        variant_cases[sequence].append(case_id)

    total_cases = len(cases)
    results = []

    for index, (sequence, count) in enumerate(
        variant_counts.most_common(), start=1
    ):
        percentage = (
            count / total_cases * 100 if total_cases else 0
        )

        results.append({
            "variant_id": f"V{index:03d}",
            "activities": list(sequence),
            "case_count": count,
            "percentage": round(percentage, 2),
            "case_ids": variant_cases[sequence]
        })

    return results


if __name__ == "__main__":
    print("CareFlow pathway discovery module is ready.")
    print("Call discover_pathways(events) with loaded event records.")
