import csv
from pathlib import Path


def export_pathways(pathways, output_file):
    """Export discovered pathway variants to a CSV file."""
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "variant_id",
        "activities",
        "case_count",
        "percentage",
        "case_ids"
    ]

    with output_path.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for pathway in pathways:
            writer.writerow({
                "variant_id": pathway.get("variant_id", ""),
                "activities": " -> ".join(
                    pathway.get("activities", [])
                ),
                "case_count": pathway.get("case_count", 0),
                "percentage": pathway.get("percentage", 0),
                "case_ids": ", ".join(pathway.get("case_ids", []))
            })

    return str(output_path)


def export_transitions(transitions, output_file):
    """Export activity transition counts to a CSV file."""
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = ["from_activity", "to_activity", "count"]

    with output_path.open(
        "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for transition in transitions:
            writer.writerow({
                "from_activity": transition.get("from_activity", ""),
                "to_activity": transition.get("to_activity", ""),
                "count": transition.get("count", 0)
            })

    return str(output_path)
