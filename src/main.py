
import argparse
import json
from pathlib import Path

from src.data_loader import load_event_log
from src.data_validator import validate_event_log
from src.pathway_mining import discover_pathways, discover_transitions
from src.dashboard_metrics import calculate_dashboard_metrics


def run_pipeline(file_path):
    """Run the complete CareFlow analysis pipeline."""
    loaded = load_event_log(file_path)

    if loaded["error"]:
        return {"error": loaded["error"]}

    events = loaded["events"]
    validation = validate_event_log(events)
    metrics = calculate_dashboard_metrics(events)
    pathways = discover_pathways(events)
    transitions = discover_transitions(events)

    return {
        "validation": validation,
        "dashboard": metrics,
        "pathways": pathways,
        "transitions": transitions
    }


def main():
    parser = argparse.ArgumentParser(
        description="CareFlow Clinical Pathway Process Mining"
    )
    parser.add_argument("csv_file", help="Path to the clinical event CSV")
    parser.add_argument(
        "--output",
        help="Optional JSON output file",
        default=None
    )
    args = parser.parse_args()

    result = run_pipeline(args.csv_file)

    if "error" in result:
        print("Error:", result["error"])
        raise SystemExit(1)

    print(json.dumps(result, indent=2, default=str))

    if args.output:
        Path(args.output).write_text(
            json.dumps(result, indent=2, default=str),
            encoding="utf-8"
        )
        print(f"Report saved to {args.output}")


if __name__ == "__main__":
    main()
  
