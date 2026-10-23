
def anonymize_case_ids(events):
    """
    Replace case IDs with anonymous IDs.
    The same original ID receives the same anonymous ID
    within this function call.
    """
    id_mapping = {}
    anonymized_events = []

    for event in events:
        new_event = event.copy()
        original_id = str(event.get("case_id", "")).strip()

        if original_id:
            if original_id not in id_mapping:
                id_mapping[original_id] = (
                    f"CASE_{len(id_mapping) + 1:03d}"
                )
            new_event["case_id"] = id_mapping[original_id]

        anonymized_events.append(new_event)

    return anonymized_events
  
