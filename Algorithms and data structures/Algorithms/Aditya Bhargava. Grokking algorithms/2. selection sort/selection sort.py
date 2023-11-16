# O(n^2)

def find_smallest(array: list):
    smallest = float("inf")
    smallest_index = 0
    for index, val in enumerate(array):
        if val < smallest:
            smallest = val
            smallest_index = index
    return smallest_index


def selection_sort(array: list):
    new_array = []
    for _ in range(len(array)):
        smallest = find_smallest(array)
        item = array.pop(smallest)
        new_array.append(item)

    return new_array


print(selection_sort([5, 777, 3, 6, 2, -94, 10]))
