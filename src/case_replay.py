from datetime import datetime


def parse_event_time(value):
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%d-%m-%Y %H:%M"
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue

    raise ValueError(f"Unsupported timestamp: {value}")


def build_case_replay(events, case_id):
    case_events = [
        event for event in events
        if event.get("case_id") == case_id
    ]

    if not case_events:
        return []

    case_events.sort(
        key=lambda event: parse_event_time(event["timestamp"])
    )

    start_time = parse_event_time(
        case_events[0]["timestamp"]
    )

    replay = []

    for index, event in enumerate(case_events):
        current_time = parse_event_time(event["timestamp"])

        previous_gap = 0

        if index > 0:
            previous_time = parse_event_time(
                case_events[index - 1]["timestamp"]
            )
            previous_gap = (
                current_time - previous_time
            ).total_seconds() / 60

        replay.append({
            "step": index + 1,
            "case_id": case_id,
            "activity": event["activity"],
            "timestamp": event["timestamp"],
            "minutes_from_start": (
                current_time - start_time
            ).total_seconds() / 60,
            "gap_from_previous_minutes": previous_gap
        })

    return replay
