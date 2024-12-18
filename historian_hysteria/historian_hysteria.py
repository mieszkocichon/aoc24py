from monads.maybe import Just, Nothing
from utils.load_file import read_file
from utils.calc_distance import calc_distance
from utils.convert_to_touples import convert_to_touples_line_splitlines
from utils.is_touples_are_digit import is_touples_are_digit
from utils.whether_lists_have_same_lenght import whether_lists_have_same_lenght
from utils.is_it_touples import is_it_touples


def sorted_distances_touple(file_path):
    return Just(file_path) \
        .bind(read_file) \
        .bind(is_touples_are_digit) \
        .bind(convert_to_touples_line_splitlines) \
        .bind(whether_lists_have_same_lenght) \
        .bind(is_it_touples) \
        .bind(lambda e: Just((sorted(e[0]), sorted(e[1]))))


def get_total_distance(file_path):
    sorted_distances = sorted_distances_touple(file_path)

    distances_between_lists = Just(sorted_distances) \
        .bind(calc_distance)

    total_distance = Just(distances_between_lists) \
        .bind(lambda e: Just(sum(e)))

    return total_distance


def create_dictionary_of_duplications(elements):
    dictionary = {}

    for x in elements:
        if x in dictionary:
            dictionary[x] = dictionary[x] + 1
        else:
            dictionary[x] = 1
        
    return Just(dictionary)


def get_locations_similarity(file_path):
    sorted_distances = sorted_distances_touple(file_path)

    dictinary_two = create_dictionary_of_duplications(sorted_distances.get_value()[1])

    sum_parts = [];

    for value in sorted_distances.get_value()[0]:
        if value in dictinary_two.get_value():
            sum_parts.append(value * dictinary_two.get_value()[value])

    return Just(sum_parts)