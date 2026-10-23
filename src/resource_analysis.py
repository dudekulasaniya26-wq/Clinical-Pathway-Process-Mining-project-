def analyze_resource_workload(events):
    workload = {}

    for event in events:
        resource = str(event.get("resource", "")).strip()

        if not resource:
            resource = "Unknown"

        workload[resource] = workload.get(resource, 0) + 1

    result = []

    for resource, event_count in sorted(workload.items()):
        result.append({
            "resource": resource,
            "event_count": event_count
        })

    return result
