class Either:
    def __init__(self, value):
        self.value = value

    def is_left(self):
        return isinstance(self, Left)

    def is_right(self):
        return isinstance(self, Right)

    def bind(self, func):
        if self.is_left():
            return self
        else:
            return func(self.value)

class Left(Either):
    pass

class Right(Either):
    pass
