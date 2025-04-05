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
    count_zero = arr.count(0)
    i = n - 1
    j = n - 1 + count_zero  # 'virtual' extended index

    while i >= 0:
        if j < n:
            arr[j] = arr[i]
        j -= 1

        if arr[i] == 0:
            if j < n:
                arr[j] = 0
            j -= 1

        i -= 1


# Example usage:
arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr1)
print(arr1)  # Output: [1,0,0,2,3,0,0,4]

arr2 = [1, 2, 3]
duplicate_zeros(arr2)
print(arr2)  # Output: [1,2,3]
