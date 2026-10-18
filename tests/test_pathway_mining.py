import unittest

from src.pathway_mining import discover_pathways


class TestPathwayMining(unittest.TestCase):

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
                "activity": "Consultation",
                "timestamp": "2026-10-10 10:15:00"
            },
            {
                "case_id": "C002",
                "activity": "Registration",
                "timestamp": "2026-10-10 09:15:00"
            },
            {
                "case_id": "C003",
                "activity": "Registration",
                "timestamp": "2026-10-10 11:00:00"
            },
            {
                "case_id": "C003",
                "activity": "Consultation",
                "timestamp": "2026-10-10 12:00:00"
            }
        ]

    def test_identifies_unique_variants(self):
        results = discover_pathways(self.events)
        self.assertEqual(len(results), 1)

    def test_counts_cases_in_variant(self):
        results = discover_pathways(self.events)
        self.assertEqual(results[0]["case_count"], 3)

    def test_variant_percentage(self):
        results = discover_pathways(self.events)
        self.assertEqual(results[0]["percentage"], 100.0)

    def test_activities_are_chronological(self):
        results = discover_pathways(self.events)
        self.assertEqual(
            results[0]["activities"],
            ["Registration", "Consultation"]
        )

    def test_empty_input(self):
        self.assertEqual(discover_pathways([]), [])


if __name__ == "__main__":
    unittest.main()
