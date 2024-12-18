from monads.maybe import Just, Nothing
from utils.load_file import read_file

def get_ceres_search(file_path, word):
    uppered_worlds = word.upper()

    content = Just(file_path) \
        .bind(read_file) \
        .bind(lambda element: Just(replaced_based_on_world(element, uppered_worlds))) \
        .bind(lambda element: Just(element.splitlines())) \
        .orElse([])

    return None




def replaced_based_on_world(content, world):
    content = ''.join([char if char in list(world) else '1' for char in content])

    return content