def binary_search_recursive(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return False

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid - 1)
    return binary_search_recursive(arr, elem, mid + 1, end)


my_list = [1, 3, 5, 7, 9]
print(binary_search_recursive(my_list, 9))  # 4
