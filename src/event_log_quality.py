
import pandas as pd


REQUIRED_COLUMNS = [
    "case_id",
    "activity",
    "timestamp"
]


def check_event_log_quality(df):
    """Check the basic quality of a clinical event log."""

    results = {
        "total_events": len(df),
        "missing_columns": [],
        "missing_case_ids": 0,
        "missing_activities": 0,
        "invalid_timestamps": 0,
        "duplicate_events": 0,
        "is_valid": True
    }

    results["missing_columns"] = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if results["missing_columns"]:
        results["is_valid"] = False
        return results

    results["missing_case_ids"] = int(
        df["case_id"].isna().sum()
    )

    results["missing_activities"] = int(
        df["activity"].isna().sum()
    )

    timestamps = pd.to_datetime(
        df["timestamp"],
        errors="coerce"
    )

    results["invalid_timestamps"] = int(
        timestamps.isna().sum()
    )

    results["duplicate_events"] = int(
        df.duplicated(
            subset=["case_id", "activity", "timestamp"]
        ).sum()
    )

    if (
        results["missing_case_ids"] > 0
        or results["missing_activities"] > 0
        or results["invalid_timestamps"] > 0
    ):
        results["is_valid"] = False

    return results
  
