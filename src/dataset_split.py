
def split_event_log(events, test_ratio=0.2):
    """Split events by case ID into training and testing sets."""
    if not 0 < test_ratio < 1:
        raise ValueError("test_ratio must be between 0 and 1")

    cases = sorted({
        event["case_id"]
        for event in events
        if event.get("case_id")
    })

    if len(cases) < 2:
        raise ValueError("At least two cases are required")

    test_count = max(1, round(len(cases) * test_ratio))
    test_cases = set(cases[-test_count:])

    train_data = [
        event for event in events
        if event.get("case_id") not in test_cases
    ]

    test_data = [
        event for event in events
        if event.get("case_id") in test_cases
    ]

    return {
        "train": train_data,
        "test": test_data
  }
  
