CareFlow Pathway Discovery Algorithm

1. Objective

Define an algorithm for identifying clinical pathway sequences from a validated event log.

2. Input

A validated event log containing:

- case_id
- activity
- timestamp

3. Algorithm

1. Receive the validated event log.
2. Group events by case_id.
3. Sort events within each case by timestamp.
4. Extract the ordered activity sequence for every case.
5. Represent each sequence as a pathway variant.
6. Count how many cases follow each variant.
7. Calculate each variant's percentage of all eligible cases.
8. Sort variants by descending frequency.
9. Return the variant table for dashboard visualization.

4. Example

Case C001:
Registration → Initial Assessment → Laboratory Test → Consultation → Discharge

Case C002:
Registration → Initial Assessment → Consultation → Discharge

These cases follow different pathway variants because their activity sequences differ.

5. Expected Output

The analysis should produce a table with:

- Variant identifier
- Ordered activity sequence
- Number of cases
- Percentage of eligible cases

6. Calculation

Variant percentage = (Number of cases in the variant / Total eligible cases) × 100.

The percentages should sum to approximately 100%, allowing for rounding, when every eligible case is assigned to exactly one variant.

7. Edge Cases

- Empty event logs.
- Cases with only one activity.
- Missing case identifiers.
- Invalid timestamps.
- Multiple events with identical timestamps.
- Duplicate event records.

Ambiguous timestamp ordering should be documented rather than guessed.

8. Interpretation

A frequent pathway is a commonly observed activity sequence. Frequency alone does not establish that the pathway is clinically appropriate or superior to another pathway.

9. Implementation Status

This document describes the algorithm. The executable implementation and tests will be added in later tasks.
