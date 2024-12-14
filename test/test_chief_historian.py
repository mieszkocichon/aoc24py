import unittest
from monads.maybe import Just, Nothing
from historian_hysteria.historian_hysteria import sorted_distances_touple, create_dictionary_of_duplications, get_locations_similarity, get_total_distance


class TestChiefHistorian(unittest.TestCase):
    def test_find_locations(self):
        file_path = 'chief_historian_locations'

        total_distance = get_total_distance(file_path)

        self.assertEqual(total_distance.get_value(), 1765812)
    

    def test_locations_similarity(self):
        file_path = 'chief_historian_locations'

        sum_parts = get_locations_similarity(file_path)

        self.assertEqual(sum(sum_parts.get_value()), 20520794)


if __name__ == '__main__':
    unittest.main()