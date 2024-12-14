from collections import Counter

def whether_level_is_unchanging(array):
    instability_level = set()

    for index, element in enumerate(array):
        if index > 0:
            if element > array[index - 1]:
                instability_level.add(True)
            elif element < array[index - 1]: 
                instability_level.add(False)

    counter = Counter(instability_level)

    return len(instability_level) == 1