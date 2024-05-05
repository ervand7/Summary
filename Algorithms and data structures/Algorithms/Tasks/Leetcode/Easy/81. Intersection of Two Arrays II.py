from typing import List


# my solution
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    h1, h2 = {}, {}
    for i in nums1:
        h1[i] = h1.get(i, 0) + 1

    for i in nums2:
        h2[i] = h2.get(i, 0) + 1

    result = []
    for k, v in h1.items():
        temp = h2.get(k)
        if temp:
            result.extend([k] * v) if v < temp else result.extend([k] * temp)

    return result


# ChatGPT solution
def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    # Count the occurrences of each element in nums1
    counts = {}
    for num in nums1:
        counts[num] = counts.get(num, 0) + 1

    # Find the intersection
    intersection = []
    for num in nums2:
        if num in counts and counts[num] > 0:
            intersection.append(num)
            counts[num] -= 1

    return intersection
