import unittest
import os
from datetime import datetime

from scheduler import get_shift_for_user, get_schedule_for_user
from exporter import export_schedule_to_csv

class TestShiftScheduler(unittest.TestCase):

    def test_get_shift_for_user(self):
        # Menguji shift berdasarkan tanggal tertentu
        self.assertEqual(get_shift_for_user("Ahmad", datetime.strptime("2024-12-26", "%Y-%m-%d").date()), "P")  # index 0
        self.assertEqual(get_shift_for_user("Vidi", datetime.strptime("2025-01-02", "%Y-%m-%d").date()), "S")   # index 7 % 7 = 0
        self.assertEqual(get_shift_for_user("Yono", datetime.strptime("2024-12-28", "%Y-%m-%d").date()), "P")   # index 2
        self.assertEqual(get_shift_for_user("Yohan", datetime.strptime("2025-01-09", "%Y-%m-%d").date()), "L")  # index 14 % 14 = 0

    def test_get_schedule_for_user(self):
        # Menguji penjadwalan rentang tanggal
        result = get_schedule_for_user("Ahmad", "2024-12-26", "2024-12-28")
        expected = {
            "2024-12-26": "P",
            "2024-12-27": "P",
            "2024-12-28": "S"
        }
        self.assertEqual(result, expected)

    def test_export_schedule_to_csv(self):
        # Menguji ekspor CSV
        filename = "test_jadwal.csv"
        user_list = ["Ahmad", "Vidi", "Yono", "Yohan"]
        export_schedule_to_csv(user_list, "2024-12-26", "2024-12-28", filename)
        self.assertTrue(os.path.exists(filename))

        with open(filename, "r") as f:
            lines = f.readlines()

        self.assertGreaterEqual(len(lines), 5)  # 1 baris header + 4 user
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
