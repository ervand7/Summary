# O(n log n)
# can merge even not sorted lists because merge_sorted_lists receives only
# previously sorted lists.
# This is the most fast sorting algorithm.
from typing import List


def sort_array(nums: List[int]) -> List[int]:
    def rec(nums: List[int]):
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left = rec(nums[:mid])
        right = rec(nums[mid:])
        return merge_sorted(left, right)

    def merge_sorted(left: List[int], right: List[int]) -> List[int]:
        i = j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += left[i:]
        result += right[j:]
        return result

    return rec(nums)


print(sort_array([999, 8, 8, 54, 3, 5, 10, 11, 4, 5, 12, 65, 76, 87, 16, 19, ]))
# [3, 4, 5, 5, 8, 8, 10, 11, 12, 16, 19, 54, 65, 76, 87, 999]
