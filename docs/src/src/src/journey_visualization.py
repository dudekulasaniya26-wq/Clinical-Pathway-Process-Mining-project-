def prepare_journey_visualization(journey):
    """Prepare patient journey records for a timeline visualization."""
    visualization = []

    for index, event in enumerate(journey, start=1):
        visualization.append({
            "step": index,
            "activity": event.get("activity", "Unknown"),
            "timestamp": event.get("timestamp", ""),
            "elapsed_seconds": event.get("elapsed_seconds"),
            "elapsed_minutes": (
                round(event["elapsed_seconds"] / 60, 2)
                if event.get("elapsed_seconds") is not None
                else None
            )
        })

    return visualization
