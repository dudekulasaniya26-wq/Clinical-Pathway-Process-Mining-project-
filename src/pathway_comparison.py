
def compare_pathways(pathway_a, pathway_b):
    """Compare two pathways represented as activity lists."""
    activities_a = pathway_a.get("activities", [])
    activities_b = pathway_b.get("activities", [])

    set_a = set(activities_a)
    set_b = set(activities_b)

    common_activities = sorted(set_a & set_b)
    only_in_a = sorted(set_a - set_b)
    only_in_b = sorted(set_b - set_a)

    return {
        "common_activities": common_activities,
        "only_in_pathway_a": only_in_a,
        "only_in_pathway_b": only_in_b,
        "same_sequence": activities_a == activities_b,
        "pathway_a_length": len(activities_a),
        "pathway_b_length": len(activities_b)
    }
  
