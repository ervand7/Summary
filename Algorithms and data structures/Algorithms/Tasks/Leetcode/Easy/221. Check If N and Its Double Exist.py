# ChatGPT solution
def binary_search(arr, target, exclude_index):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target and mid != exclude_index:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def check_if_exist(arr):
    arr.sort()  # Step 1: Sort the array

    for i, num in enumerate(arr):
        if binary_search(arr, num * 2, i):  # Step 2: Search for 2 * num
            return True

    return False
