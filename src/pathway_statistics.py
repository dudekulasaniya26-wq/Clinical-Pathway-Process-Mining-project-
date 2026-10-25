
from collections import Counter


def calculate_pathway_statistics(pathways):
    """
    pathways: list of dictionaries containing
    case_id and activities.
    """
    counts = Counter()
    case_count = 0

    for pathway in pathways:
        case_id = str(pathway.get("case_id", "")).strip()
        activities = pathway.get("activities", [])

        if not case_id or not activities:
            continue

        pathway_key = tuple(activities)
        counts[pathway_key] += 1
        case_count += 1

    results = []

    for index, (activities, count) in enumerate(
        counts.most_common(), start=1
    ):
        results.append({
            "rank": index,
            "activities": list(activities),
            "case_count": count,
            "percentage": round(count / case_count * 100, 2)
        })

    return {
        "total_cases": case_count,
        "unique_pathways": len(counts),
        "pathway_statistics": results,
        "most_common_pathway": results[0] if results else None
      }
  
