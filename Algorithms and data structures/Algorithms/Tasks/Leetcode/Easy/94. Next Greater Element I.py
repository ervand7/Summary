from typing import List


# my solution
def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    h = {}
    for i in range(1, len(nums2)):
        temp = -1
        for j in range(i, len(nums2)):
            if nums2[j] > nums2[i - 1]:
                temp = nums2[j]
                break
        h[nums2[i - 1]] = temp
    h[nums2[-1]] = -1

    result = []
    for i in nums1:
        result.append(h[i])

    return result


# ChatGPT solution
def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    next_greater = {}
    stack = []

    for num in nums2:
        while stack and num > stack[-1]:
            next_greater[stack.pop()] = num
        stack.append(num)

    while stack:
        next_greater[stack.pop()] = -1

    ans = [next_greater[num] for num in nums1]
    return ans


next_greater_element(nums1=[4, 1, 2], nums2=[1, 3, 4, 2])
