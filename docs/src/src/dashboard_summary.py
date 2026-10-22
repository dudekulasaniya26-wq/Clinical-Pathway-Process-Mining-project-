def format_dashboard_summary(metrics):
    """Convert dashboard metrics into a readable text report."""
    lines = [
        "CAREFLOW - CLINICAL DASHBOARD SUMMARY",
        "=" * 42,
        f"Total cases: {metrics.get('total_cases', 0)}",
        f"Total events: {metrics.get('total_events', 0)}",
        f"Distinct activities: {metrics.get('distinct_activities', 0)}",
        "",
        "ACTIVITY FREQUENCY",
        "-" * 24
    ]

    frequencies = metrics.get("activity_frequency", {})

    if frequencies:
        for activity, count in sorted(
            frequencies.items(),
            key=lambda item: (-item[1], item[0])
        ):
            lines.append(f"{activity}: {count}")
    else:
        lines.append("No activity data available.")

    lines.extend([
        "",
        "CASE DURATION (SECONDS)",
        "-" * 24
    ])

    duration_fields = [
        ("Average", "average_case_duration_seconds"),
        ("Minimum", "minimum_case_duration_seconds"),
        ("Maximum", "maximum_case_duration_seconds"),
        ("Median", "median_case_duration_seconds")
    ]

    for label, key in duration_fields:
        value = metrics.get(key)
        display_value = f"{value:.2f}" if value is not None else "N/A"
        lines.append(f"{label}: {display_value}")

    return "\n".join(lines)


def save_dashboard_summary(metrics, output_file):
    """Save the formatted dashboard summary to a text file."""
    summary = format_dashboard_summary(metrics)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(summary + "\n")

    return output_file
