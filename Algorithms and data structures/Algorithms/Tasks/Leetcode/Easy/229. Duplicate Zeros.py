from typing import List


# my solution
def duplicate_zeros(arr: List[int]) -> None:
    i = 0
    len_arr = len(arr)
    while i < len_arr - 1:
        if arr[i] == 0:
            if i == len_arr - 2:
                arr[-1] = 0
                return
            arr[i + 2:] = arr[i + 1: -1]
            arr[i + 1] = 0
            i += 2
        else:
            i += 1


# ChatGPT solution
def duplicate_zeros(arr):
    n = len(arr)

    # Count how many zeros are in the array
    # because each zero will take one extra space when duplicated
    count_zero = arr.count(0)

    # i is the index for reading the original array (from end to start)
    i = n - 1

    # j is the index for writing into the "virtual extended array"
    j = n - 1 + count_zero

    while i >= 0:
        # If j is within bounds, write arr[i] to arr[j]
        # (we only write when j is inside the actual array)
        if j < n:
            arr[j] = arr[i]
        j -= 1

        # If the current element is zero, we need to write it twice
        if arr[i] == 0:
            if j < n:
                arr[j] = 0
            j -= 1

        # Move to the previous element in the original array
        i -= 1


# Example usage:
arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr1)
print(arr1)  # Output: [1,0,0,2,3,0,0,4]

arr2 = [1, 2, 3]
duplicate_zeros(arr2)
print(arr2)  # Output: [1,2,3]
