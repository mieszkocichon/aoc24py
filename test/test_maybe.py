import unittest
from monads.maybe import Just, Nothing

def divide(x, y):
    if y == 0:
        return Nothing()
    else:
        return Just(x / y)

def add_five(x):
    return Just(x + 5)

def multiply_by_two(x):
    return Just(x * 2)

class TestMaybe(unittest.TestCase):
    
    def test_divide_add_and_multiply(self):
        result = Just(10) \
            .bind(lambda x: divide(x, 2)) \
            .bind(add_five) \
            .bind(multiply_by_two) 

        self.assertEqual(result.get_value(), 20)

    def test_or_else(self):
        result = Just(10).bind(lambda x: divide(x, 0)).orElse(42)

        self.assertEqual(result.get_value(), 42)

if __name__ == '__main__':
    unittest.main()