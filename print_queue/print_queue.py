
def print_queue(file_path):
    ordered_list, number_of_pages = open(file_path).read().split('\n\n')
    ordered_list = [tuple(int(part) for part in line.split('|')) for line in ordered_list.splitlines()]
    number_of_pages = [list(map(int, line.split(','))) for line in number_of_pages.splitlines()]

    correct_ordered_list = []

    incorrect_ordered_list = []

    for pages in number_of_pages:
        res = iterate_list(pages, ordered_list, True)
        if res[1] == True:
            correct_ordered_list.append(res[0])
        else:
            incorrect_ordered_list.append(res[0])

    return (correct_ordered_list, incorrect_ordered_list)



def iterate_list(elements, ordered_list, is_sortable):
    for ordered_tuple in ordered_list:
        if ordered_tuple[0] in elements and ordered_tuple[1] in elements:
            if elements.index(ordered_tuple[0]) > elements.index(ordered_tuple[1]):
                elements.insert(elements.index(ordered_tuple[1]), elements.pop(elements.index(ordered_tuple[0])))

                return iterate_list(elements, ordered_list, False)

    return (elements, is_sortable)