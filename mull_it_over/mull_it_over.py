
import re
from monads.maybe import Just, Nothing
from utils.load_file import read_file

def get_valid_operations(file_path):
    result = Just(file_path) \
        .bind(read_file) \
        .bind(process_instructions) \
        .bind(lambda e: Just(sum(e))) \
        .orElse(0)

    return result

def safe_int_conversion_touple(string_value):
    try:
        return Just((int(string_value[0]), int(string_value[1])))
    except ValueError:
        return Nothing

def parse_instructions(memory):
    pattern = r"mul\((\d+),(\d+)\)"
    return [(int(x), int(y)) for x, y in re.findall(pattern, memory)]

def process_instructions(string):
    instructions = re.split(r"(do\(\)|don't\(\))", string)

    enabled = True
    elements = []

    for section in instructions:
        if "mul" in section:
            if enabled:
                muls = parse_instructions(section)
                elements.append(sum(x * y for x, y in muls))
        elif "do()" in section:
            enabled = True
        elif "don't()" in section:
            enabled = False

    return Just(elements)

