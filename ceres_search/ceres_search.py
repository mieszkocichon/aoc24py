from monads.maybe import Just, Nothing
from utils.load_file import read_file

def get_ceres_search(file_path):
    first_line_height = 0

    content = Just(file_path) \
        .bind(read_file) \
        .bind(lambda element: Just(element.splitlines()))

    first_line_height = len(content.get_value()[0])

    return content.bind(lambda elements: validate_list_length(elements, first_line_height)) \
        .bind(lambda elements: calculate(elements))

def validate_list_length(elements, first_line_height):
    for element in elements:
        if len(element) != first_line_height:
            return Nothing

    return Just(elements)

def calculate(lists):
    return [
        tuple for tuple in get_xmas_neighbors_touples(lists)
        if all('M' in element and 'A' in element and 'S' in element for element in tuple)
    ]

def get_xmas_neighbors_touples(lists):
    return [
        (
            (lists[list_number - 1][element_position - 1]
             + element
             + lists[list_number + 1][element_position + 1],

            lists[list_number - 1][element_position + 1]
            + element
            + lists[list_number + 1][element_position - 1])
        )
        for list_number, sub_list in enumerate(lists[1:-1], 1)
        for element_position, element in enumerate(sub_list[1:-1], 1)
        if element == "A"
    ]