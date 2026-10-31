from collections import Counter, defaultdict
from datetime import datetime


def calculate_resource_transitions(events):
    """Count transitions between consecutive resources."""
    grouped = defaultdict(list)

    for event in events:
        case_id = str(event.get("case_id", "")).strip()
        resource = str(event.get("resource", "")).strip()

        if not case_id or not resource:
            continue

        try:
            timestamp = datetime.strptime(
                event.get("timestamp", ""),
                "%Y-%m-%d %H:%M:%S"
            )
        except (ValueError, TypeError):
            continue

        grouped[case_id].append((timestamp, resource))

    transitions = Counter()

    for records in grouped.values():
        records.sort(key=lambda item: item[0])

        for index in range(1, len(records)):
            previous = records[index - 1][1]
            current = records[index][1]

            if previous != current:
                transitions[(previous, current)] += 1

    return [
        {
            "from_resource": source,
            "to_resource": target,
            "transition_count": count
        }
        for (source, target), count in transitions.most_common()
    ]
