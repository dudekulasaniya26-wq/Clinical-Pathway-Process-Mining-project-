from collections import Counter, defaultdict
from itertools import combinations


def analyze_activity_cooccurrence(events):
    """Count activity pairs appearing in the same case."""
    case_activities = defaultdict(set)

    for event in events:
        case_id = str(event.get("case_id", "")).strip()
        activity = str(event.get("activity", "")).strip()

        if case_id and activity:
            case_activities[case_id].add(activity)

    pair_counts = Counter()

    for activities in case_activities.values():
        for pair in combinations(sorted(activities), 2):
            pair_counts[pair] += 1

    return [
        {
            "activity_one": pair[0],
            "activity_two": pair[1],
            "case_count": count
        }
        for pair, count in pair_counts.most_common()
    ]
