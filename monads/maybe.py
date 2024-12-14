class Maybe:
    def is_nothing(self):
        return False
    
    def is_just(self):
        return False

    def bind(self, func):
        raise NotImplementedError

    def map(self, func):
        raise NotImplementedError

    def get_value(self):
        raise NotImplementedError

    def orElse(self, default):
        raise NotImplementedError


class Just(Maybe):
    def __init__(self, value):
        self.value = value
    
    def is_just(self):
        return True

    def bind(self, func):
        return func(self.value)

    def map(self, func):
        return Just(func(self.value))

    def get_value(self):
        return self.value

    def orElse(self, default):
        return self


class Nothing(Maybe):
    def is_nothing(self):
        return True
    
    def bind(self, func):
        return self
    
    def map(self, func):
        return self
    
    def get_value(self):
        raise ValueError("Cannot get value from Nothing.")
    
    def orElse(self, default):
        return Just(default)
