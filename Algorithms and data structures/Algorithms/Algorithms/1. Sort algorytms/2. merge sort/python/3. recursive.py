# O(n log n)
# can merge even not sorted lists because merge_sorted_lists receives only
# previously sorted lists


def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        middle = len(array) // 2
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])
        return merge_sorted_lists(left, right)


def merge_sorted_lists(first: list, second: list):
    result = []
    i = j = 0
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1

    # at this point there can be at most one of the lists left
    result += first[i:]
    result += second[j:]
    return result


print(merge_sort([999, 8, 8, 54, 3, 5, 10, 11, 4, 5, 12, 65, 76, 87, 16, 19, ]))
# [3, 4, 5, 5, 8, 8, 10, 11, 12, 16, 19, 54, 65, 76, 87, 999]
