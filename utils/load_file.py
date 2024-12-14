from monads.maybe import Just, Nothing

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read();
            return Just(content)
    except FileNotFoundError:
        return Nothing