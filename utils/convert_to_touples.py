from monads.maybe import Just, Nothing

def convert_to_touples(content):
    lines = content.splitlines()

    column_one = []
    column_two = []

    for line in lines:
        num1, num2 = line.split()

        column_one.append(int(num1))
        column_two.append(int(num2))

    return Just((column_one, column_two))

