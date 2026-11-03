from datetime import datetime


def get_case_sequence(events, case_id):
    case_events = [
        event for event in events
        if event.get("case_id") == case_id
    ]

    case_events.sort(
        key=lambda event: datetime.strptime(
            event["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )
    )

    return [
        event["activity"] for event in case_events
    ]


def compare_case_sequences(events, case_a, case_b):
    sequence_a = get_case_sequence(events, case_a)
    sequence_b = get_case_sequence(events, case_b)

    first_difference = None

    for index in range(
        min(len(sequence_a), len(sequence_b))
    ):
        if sequence_a[index] != sequence_b[index]:
            first_difference = {
                "step": index + 1,
                "activity_a": sequence_a[index],
                "activity_b": sequence_b[index]
            }
            break

    if first_difference is None and (
        len(sequence_a) != len(sequence_b)
    ):
        index = min(len(sequence_a), len(sequence_b))

        first_difference = {
            "step": index + 1,
            "activity_a": (
                sequence_a[index]
                if index < len(sequence_a) else "No activity"
            ),
            "activity_b": (
                sequence_b[index]
                if index < len(sequence_b) else "No activity"
            )
        }

    return {
        "case_a": case_a,
        "case_b": case_b,
        "sequence_a": sequence_a,
        "sequence_b": sequence_b,
        "same_sequence": sequence_a == sequence_b,
        "first_difference": first_difference
    }
