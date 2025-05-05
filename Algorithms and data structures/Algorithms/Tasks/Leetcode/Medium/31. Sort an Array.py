from typing import List


# my solution
# this is just simple merge sort algorithm implementation
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
