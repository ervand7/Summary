from typing import List


def canThreePartsEqualSum(arr: List[int]) -> bool:
    for i in range(len(arr) - 2):
        i_sum = sum(arr[:i + 1])
        for j in range(i + 1, len(arr) - 1):
            j_sum = sum(arr[i + 1:j + 1])
            if j_sum == i_sum:
                for e in range(j + 1, len(arr)):
                    e_sum = sum(arr[j + 1:e]) + arr[e]
                    if e_sum == j_sum:
                        if e == len(arr) - 1:
                            return True

    return False


print(canThreePartsEqualSum([1, 1, 1, 1]))
