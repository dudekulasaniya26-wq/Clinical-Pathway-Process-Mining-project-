def calculate_conformance_score(observed, reference):
    """
    Compare an observed activity sequence with a reference sequence.
    Returns a percentage based on matching activity positions.
    """
    if not reference:
        return {
            "matching_activities": 0,
            "total_reference_activities": 0,
            "conformance_percentage": 0.0
        }

    matching = sum(
        1 for index, activity in enumerate(reference)
        if index < len(observed) and observed[index] == activity
    )

    percentage = (matching / len(reference)) * 100

    return {
        "matching_activities": matching,
        "total_reference_activities": len(reference),
        "conformance_percentage": round(percentage, 2)
    }
