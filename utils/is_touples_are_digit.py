from monads.maybe import Just, Nothing

is_touples_are_digit = lambda e: Nothing if not [line.split()[0].isdigit() and line.split()[1].isdigit() for line in e.splitlines()] else Just(e)