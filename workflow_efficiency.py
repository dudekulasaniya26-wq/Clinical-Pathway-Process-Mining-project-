def calculate_efficiency_score(actual_minutes, expected_minutes):
    """Compare actual duration with an expected duration."""
    if actual_minutes < 0 or expected_minutes <= 0:
        raise ValueError(
            "Actual duration must be non-negative and "
            "expected duration must be positive."
        )

    if actual_minutes == 0:
        return 100.0

    score = (expected_minutes / actual_minutes) * 100
    return round(min(score, 100.0), 2)


def classify_efficiency(score):
    """Assign a simple label to an efficiency score."""
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 80:
        return "Efficient"
    elif score >= 50:
        return "Needs review"
    else:
        return "Low efficiency"
