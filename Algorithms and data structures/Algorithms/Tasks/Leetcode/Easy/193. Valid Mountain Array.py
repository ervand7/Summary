from typing import List


# my solution
def valid_mountain_array(arr: List[int]) -> bool:
    go_high = True

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return False

        if go_high:
            if arr[i] < arr[i - 1]:
                if i == 1:
                    return False
                go_high = False

        else:
            if arr[i] > arr[i - 1]:
                return False

    return go_high is False
