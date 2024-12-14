from monads.maybe import Just

convert_rows_strings_to_ints_list = lambda e: Just([[int(x) for x in line.split()] for line in e.splitlines()])
