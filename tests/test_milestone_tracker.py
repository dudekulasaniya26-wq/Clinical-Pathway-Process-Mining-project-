import unittest

from src.milestone_tracker import (
    track_case_milestones,
    calculate_milestone_progress
)

from src.case_completion_report import (
    generate_case_completion_report
)


class TestMilestoneTracker(unittest.TestCase):

    def setUp(self):
        self.events = [
            {
                "case_id": "C001",
                "activity": "Registration"
            },
            {
                "case_id": "C001",
                "activity": "Doctor Consultation"
            },
            {
                "case_id": "C001",
                "activity": "Lab Test"
            },
            {
                "case_id": "C002",
                "activity": "Registration"
            }
        ]

    def test_milestone_tracking(self):
        result = track_case_milestones(
            self.events, "C001"
        )

        self.assertTrue(result[0]["completed"])
        self.assertFalse(result[3]["completed"])

    def test_progress_percentage(self):
        result = calculate_milestone_progress(
            self.events, "C001"
        )

        self.assertEqual(
            result["completed_milestones"], 3
        )
        self.assertEqual(
            result["progress_percentage"], 60.0
        )

    def test_unknown_case(self):
        result = calculate_milestone_progress(
            self.events, "C999"
        )

        self.assertEqual(
            result["completed_milestones"], 0
        )
        self.assertEqual(
            result["progress_percentage"], 0.0
        )

    def test_completion_report(self):
        reports = generate_case_completion_report(
            self.events
        )

        self.assertEqual(len(reports), 2)
        self.assertEqual(
            reports[0]["status"], "Pending"
        )

    def test_pending_activities(self):
        reports = generate_case_completion_report(
            self.events
        )

        self.assertIn(
            "Treatment",
            reports[0]["pending_activities"]
        )


if __name__ == "__main__":
    unittest.main()
