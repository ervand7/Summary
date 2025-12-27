from typing import List


def find_array(pref: List[int]) -> List[int]:
    n = len(pref)
    result = [0] * n
    result[0] = pref[0]
    for i in range(1, n):
        result[i] = pref[i - 1] ^ pref[i]

    return result


print(find_array([5, 2, 0, 3, 1]))
