import unittest
from red_nosed_reports.red_nosed_reports import get_filtered_reports

class TestRedNosedScenario(unittest.TestCase):
    def test_find_locations(self):
        file_path = 'red_nosed_report'

        content = get_filtered_reports(file_path)

        self.assertEqual(len(content), 285)


if __name__ == '__main__':
    unittest.main()