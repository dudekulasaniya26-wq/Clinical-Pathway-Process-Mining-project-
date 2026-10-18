# CareFlow Dashboard Metrics

## 1. Purpose

This document defines the initial metrics that will be displayed in the CareFlow dashboard.

## 2. Core Metrics

### Total Cases
Count the number of distinct case_id values in the validated event log.

### Total Events
Count the number of valid event records.

### Distinct Activities
Count the number of unique activity names.

### Pathway Variants
Group cases that follow the same ordered sequence of activities. Count the distinct sequences.

### Average Case Duration
For each case, subtract its earliest event timestamp from its latest event timestamp. Calculate the mean of valid case durations.

### Activity Frequency
Count the number of event records associated with each activity.

### Potential Waiting Time
Calculate the difference between consecutive event timestamps within each case. Interpret this as elapsed time between recorded events, not necessarily actual clinical waiting time.

## 3. Visualization Plan

- KPI cards for total cases, events, and distinct activities.
- Bar chart for activity frequency.
- Table showing common pathway variants and their case counts.
- Process flow diagram showing transitions between activities.
- Duration chart showing case durations.
- Data quality summary showing invalid or missing values.

## 4. Calculation Rules

- Exclude invalid records from metrics only according to documented validation rules.
- Report excluded records and explain why they were excluded.
- Handle missing timestamps explicitly.
- Do not calculate negative durations as valid durations.
- Do not treat missing metrics as zero.
- Display duration units consistently.

## 5. Limitations

Metrics depend on the completeness and accuracy of the event log. Recorded elapsed time may include multiple activities or other delays. These metrics describe workflow patterns and do not establish clinical quality or treatment effectiveness.
