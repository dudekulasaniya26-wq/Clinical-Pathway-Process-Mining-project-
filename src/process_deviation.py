def detect_process_deviations(observed, reference):
    """Compare an observed sequence with a reference sequence."""
    observed = list(observed)
    reference = list(reference)

    missing = [activity for activity in reference if activity not in observed]
    unexpected = [activity for activity in observed if activity not in reference]

    common_order = [activity for activity in observed if activity in reference]
    expected_order = [activity for activity in reference if activity in observed]

    return {
        "missing_activities": missing,
        "unexpected_activities": unexpected,
        "order_matches": common_order == expected_order,
        "sequence_matches": observed == reference
    }
