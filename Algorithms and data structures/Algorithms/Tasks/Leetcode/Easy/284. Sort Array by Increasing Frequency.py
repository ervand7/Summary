from typing import List


def frequency_sort(nums: List[int]) -> List[int]:
    h = {}
    for i in nums:
        h[i] = h.get(i, 0) + 1

    nums.sort(key=lambda x: (h[x], -x))
    return nums


# my alternative solution
def frequency_sort(nums: List[int]) -> List[int]:
    h = {}
    for i in nums:
        h[i] = h.get(i, 0) + 1

    h2 = {}
    for k, v in h.items():
        if h2.get(v) is None:
            h2[v] = [k]
        else:
            h2[v].append(k)

    result = []
    for count, v in sorted(h2.items(), key=lambda x: x[0]):
        value = sorted(v, reverse=True)
        temp = []
        for i in value:
            temp.extend([i] * count)
        result.extend(temp)

    return result
