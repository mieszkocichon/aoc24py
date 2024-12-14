

def has_not_adjancent_duplicates(array):
    
    for index in range(len(array) - 1):
        if (array[index] == array[index + 1]):
            return False

    return True