import unittest
from mull_it_over.mull_it_over import get_valid_operations

class TestMullItOver(unittest.TestCase):
    def test_mull_it_overs(self):
        file_path = 'mull_it_over_input'

        content = get_valid_operations(file_path)

        self.assertEqual(content.get_value(), 85508223)


if __name__ == '__main__':
    unittest.main()