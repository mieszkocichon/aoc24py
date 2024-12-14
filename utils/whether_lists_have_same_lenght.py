from monads.maybe import Just, Nothing

whether_lists_have_same_lenght = lambda e: Just(e) if len(e[0]) == len(e[1]) else Nothing