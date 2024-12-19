from monads.maybe import Just, Nothing
from utils.load_file import read_file

def get_ceres_search(file_path, word):
    uppered_worlds = word.upper()
    first_line_height = 0

    content = Just(file_path) \
        .bind(read_file) \
        .bind(lambda element: Just(element.splitlines()))

    first_line_height = len(content.get_value()[0])

    content.bind(lambda elements: validate_list_length(elements, first_line_height)) \
        .orElse([])

    return None

def validate_list_length(elements, first_line_height):
    for element in elements:
        if len(element) != first_line_height:
            return Nothing

    return Just(elements)