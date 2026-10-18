CareFlow Dashboard Wireframe

1. Purpose

The dashboard will summarize clinical process mining results and help users explore pathway variations and potential workflow delays.

2. Page Layout

Header

Display:

- Project name: CareFlow
- Subtitle: Clinical Pathway Process Mining
- Dataset status
- Data upload or selection area, depending on the final technology

Section 1: Key Performance Indicators

Display cards for:

- Total Cases
- Total Events
- Distinct Activities
- Pathway Variants
- Average Case Duration

Each card must display a calculated value from the analysis results. If a metric cannot be calculated, show an appropriate message instead of an invented value.

Section 2: Activity Frequency

Display a bar chart showing the number of recorded events for each activity.

Section 3: Pathway Variants

Display a table with:

- Variant ID
- Activity Sequence
- Number of Cases
- Percentage of Cases

Sort the table by case count in descending order.

Section 4: Process Flow

Display a process diagram illustrating transitions between consecutive activities. Transition counts should be derived from the event log.

Section 5: Duration Analysis

Display case durations and, where possible, elapsed time between consecutive recorded activities.

Clearly distinguish elapsed time between events from actual waiting time.

Section 6: Data Quality

Display:

- Number of input records
- Number of valid records
- Number of invalid records
- Missing required values
- Invalid timestamps
- Potential duplicate records

3. Proposed Filters

Provide filters for date range, activity, and department only when those fields are available.

4. User Experience

- Use readable labels.
- Display units for duration metrics.
- Show loading and error messages.
- Provide a clear empty-data state.
- Avoid displaying charts when required data is unavailable.
- Keep the layout usable on smaller screens.

5. Expected Outcome

The wireframe will serve as the reference for dashboard implementation. All displayed metrics must be connected to actual analysis results.

6. Implementation Status

This document describes the planned interface. The actual dashboard will be implemented after the team confirms the programming language and framework.
