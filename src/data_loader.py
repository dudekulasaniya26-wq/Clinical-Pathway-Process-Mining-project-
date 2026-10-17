
import csv
from datetime import datetime

REQUIRED_FIELDS = ["case_id", "activity", "timestamp"]


def load_event_log(file_path):
    """Load and parse a clinical event log from a CSV file."""
    events = []

    try:
        with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                return {"events": [], "error": "CSV file is empty."}

            headers = [
                name.strip() if name else ""
                for name in reader.fieldnames
            ]

            if len(headers) != len(set(headers)):
                return {
                    "events": [],
                    "error": "Duplicate column names found."
                }

            missing = [
                field for field in REQUIRED_FIELDS
                if field not in headers
            ]

            if missing:
                return {
                    "events": [],
                    "error": "Missing required columns: "
                    + ", ".join(missing)
                }

            for row in reader:
                event = {
                    key.strip(): (value.strip() if value else "")
                    for key, value in row.items()
                    if key is not None
                }

                try:
                    datetime.strptime(
                        event["timestamp"], "%Y-%m-%d %H:%M:%S"
                    )
                except ValueError:
                    event["_timestamp_valid"] = "false"
                else:
                    event["_timestamp_valid"] = "true"

                events.append(event)

        return {"events": events, "error": None}

    except (OSError, UnicodeError, csv.Error) as error:
        return {"events": [], "error": str(error)}


if __name__ == "__main__":
    print("CareFlow event-log loader is ready.")
    print("Call load_event_log(file_path) to load a CSV file.")
          
