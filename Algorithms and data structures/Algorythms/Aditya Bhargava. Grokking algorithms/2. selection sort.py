def find_smallest(array: list):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array: list):
    """O(n^2)"""
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        item = array.pop(smallest)
        new_array.append(item)

    return new_array


print(selection_sort([5, 3, 6, 2, 10]))
