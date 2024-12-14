from monads.maybe import Just, Nothing

is_it_touples = lambda e: Nothing if not isinstance(e, tuple) else Just(e)