import unittest

from src.dashboard_metrics import calculate_dashboard_metrics


class TestDashboardMetrics(unittest.TestCase):

    def setUp(self):
        self.events = [
            {
                "case_id": "C001",
                "activity": "Registration",
                "timestamp": "2026-10-10 09:00:00"
            },
            {
                "case_id": "C001",
                "activity": "Consultation",
                "timestamp": "2026-10-10 10:00:00"
            },
            {
                "case_id": "C002",
                "activity": "Registration",
                "timestamp": "2026-10-10 11:00:00"
            },
            {
                "case_id": "C002",
                "activity": "Discharge",
                "timestamp": "2026-10-10 11:30:00"
            }
        ]

    def test_total_cases(self):
        result = calculate_dashboard_metrics(self.events)
        self.assertEqual(result["total_cases"], 2)

    def test_total_events(self):
        result = calculate_dashboard_metrics(self.events)
        self.assertEqual(result["total_events"], 4)

    def test_distinct_activities(self):
        result = calculate_dashboard_metrics(self.events)
        self.assertEqual(result["distinct_activities"], 3)

    def test_activity_frequency(self):
        result = calculate_dashboard_metrics(self.events)
        self.assertEqual(
            result["activity_frequency"]["Registration"], 2
        )

    def test_average_case_duration(self):
        result = calculate_dashboard_metrics(self.events)
        self.assertEqual(
            result["average_case_duration_seconds"], 2700.0
        )

    def test_empty_input(self):
        result = calculate_dashboard_metrics([])
        self.assertEqual(result["total_cases"], 0)
        self.assertEqual(result["total_events"], 0)
        self.assertIsNone(
            result["average_case_duration_seconds"]
        )


if __name__ == "__main__":
    unittest.main()
