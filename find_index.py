# find a given number in a list
# list can contain under lists
# Return the list of indices this way


def index_all(list_to_search, value_to_search):
    indices_found = []
    get_index(list_to_search, value_to_search, indices_found, result_set=[])
    return indices_found


def get_index(list_to_search, value_to_search, indices_found, result_set):
    for index, item in enumerate(list_to_search, start=0):
        copy_of_result_set = result_set.copy()
        if isinstance(item, list):
            copy_of_result_set.append(index)
            get_index(item, value_to_search, indices_found, copy_of_result_set)
        else:
            if item == value_to_search:
                copy_of_result_set.append(index)
                indices_found.append(copy_of_result_set)


if __name__ == "__main__":
    print(index_all([1, 2, 2, [1, 3, 2], [3, [5, 6, 2, [2]]], 4, 5], 2))