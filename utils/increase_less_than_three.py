
def increase_less_than_three(array):
    for index, element in enumerate(array):
        if index > 0:
            if element > array[index - 1]:
                if element - array[index - 1] > 3:
                    return False

            if element < array[index - 1]:
                if array[index - 1] - element > 3:
                    return False
    
    return True