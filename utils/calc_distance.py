import copy
from monads.maybe import Just, Nothing

def calc_distance(distances_touple):
    distance_list_one = copy.deepcopy(distances_touple.value[0])
    distance_list_two = copy.deepcopy(distances_touple.value[1])

    distances_between_lists = [] 

    for item1, item2 in zip(distance_list_one, distance_list_two):
        distances_between_lists.append(abs(item1 - item2))

    return distances_between_lists