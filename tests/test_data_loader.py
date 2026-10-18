
import os
import tempfile
import unittest

from src.data_loader import load_event_log


class TestDataLoader(unittest.TestCase):

    def create_csv(self, content):
        temp = tempfile.NamedTemporaryFile(
            mode="w", suffix=".csv",
            encoding="utf-8", newline="",
            delete=False
        )
        temp.write(content)
        temp.close()
        self.addCleanup(lambda: os.path.exists(temp.name)
                        and os.remove(temp.name))
        return temp.name

    def test_load_valid_csv(self):
        path = self.create_csv(
            "case_id,activity,timestamp\n"
            "C001,Registration,2026-10-10 09:00:00\n"
        )
        result = load_event_log(path)
        self.assertIsNone(result["error"])
        self.assertEqual(len(result["events"]), 1)
        self.assertEqual(result["events"][0]["case_id"], "C001")

    def test_missing_required_column(self):
        path = self.create_csv(
            "case_id,activity\nC001,Registration\n"
        )
        result = load_event_log(path)
        self.assertIsNotNone(result["error"])
        self.assertIn("timestamp", result["error"])

    def test_invalid_timestamp_is_marked(self):
        path = self.create_csv(
            "case_id,activity,timestamp\n"
            "C001,Registration,invalid-date\n"
        )
        result = load_event_log(path)
        self.assertIsNone(result["error"])
        self.assertEqual(
            result["events"][0]["_timestamp_valid"], "false"
        )

    def test_missing_file_returns_error(self):
        result = load_event_log("missing_careflow_file.csv")
        self.assertIsNotNone(result["error"])
        self.assertEqual(result["events"], [])


if __name__ == "__main__":
    unittest.main()
          
