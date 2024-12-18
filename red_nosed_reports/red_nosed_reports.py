from utils.whether_level_is_unchanging import whether_level_is_unchanging
from utils.increase_less_than_three import increase_less_than_three
from utils.has_not_adjancent_duplicates import has_not_adjancent_duplicates
from monads.maybe import Just, Nothing
from utils.load_file import read_file
from utils.convert_rows_strings_to_ints_list import convert_rows_strings_to_ints_list

def get_filtered_reports(file_path):
    return Just(file_path) \
            .bind(read_file) \
            .bind(convert_rows_strings_to_ints_list) \
            .bind(get_problem_dumper_result)

def get_problem_dumper_result(arr):
    dumper_set = []

    for elements in arr:
        if len(filter_reports([elements[:index] + elements[index+1:] for index in range(len(elements))] + [list(elements)])) > 0:
            dumper_set.append(elements)
            
    return dumper_set

filter_reports = lambda array: [array[i] for i in range(0, len(array)) if whether_level_is_unchanging(array[i]) and increase_less_than_three(array[i]) and has_not_adjancent_duplicates(array[i])]

