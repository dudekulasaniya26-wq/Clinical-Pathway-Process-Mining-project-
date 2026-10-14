CareFlow Event Log Data Dictionary

1. Purpose

This document defines the proposed structure of the event log used by CareFlow. A consistent data format will help all project modules process the same records.

2. Required Fields

Field| Data Type| Description| Required
case_id| String| Synthetic identifier for a patient encounter or process instance| Yes
activity| String| Name of the recorded workflow activity| Yes
timestamp| DateTime| Date and time when the activity occurred| Yes

3. Optional Fields

Field| Data Type| Description
department| String| Department or service associated with an activity
resource| String| De-identified role or resource associated with an activity
activity_status| String| Recorded activity status, if available
diagnosis_group| String| Broad, non-identifying diagnosis category, if required and available

Optional fields should only be used when the dataset contains them and their use is appropriate.

4. Synthetic Example

case_id| activity| timestamp| department
C001| Registration| 2026-10-10 09:00| Reception
C001| Initial Assessment| 2026-10-10 09:20| Assessment
C001| Laboratory Test| 2026-10-10 10:00| Laboratory
C001| Consultation| 2026-10-10 11:00| Consultation
C002| Registration| 2026-10-10 09:10| Reception
C002| Initial Assessment| 2026-10-10 09:35| Assessment
C002| Consultation| 2026-10-10 10:15| Consultation

All records in this example are fictional and are provided only to demonstrate the format.

5. Data Validation Rules

1. Required column names must be present.
2. Case identifiers must not be empty.
3. Activity names must not be empty.
4. Timestamps must follow a consistent, parseable format.
5. Events within each case should be ordered by timestamp before process analysis.
6. Duplicate records should be identified and reviewed.
7. Missing or invalid values should be reported rather than silently ignored.
8. Timestamp ties should be documented because event ordering may be ambiguous.
9. Optional columns must not be assumed to exist in every dataset.

6. Data Preparation Expectations

The data preparation module should produce a validated event log and a summary of data quality issues. It should preserve the original input and document any transformations performed.

7. Privacy Requirements

Use synthetic or appropriately de-identified data. Do not commit identifiable patient information, medical record numbers, contact details, credentials, or confidential hospital records to the repository.

8. Integration Contract

The initial proposed interface uses case_id, activity, and timestamp as the required fields. The team must confirm this contract against the actual dataset before implementing processing algorithms.

Any changes to required field names or formats must be communicated to all team members.
