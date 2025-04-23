from typing import List


# my solution
def find_special_integer(arr: List[int]) -> int:
    current = arr[0]
    len_arr = len(arr)
    if len_arr == 1:
        return current

    threshold = len_arr // 4
    count = 1
    for i in arr[1:]:
        if i == current:
            count += 1
            if count > threshold:
                return i

        else:
            current = i
            count = 1
