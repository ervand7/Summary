# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def closest_nodes(root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
    def binary_search_min(arr: list, n: int) -> int:
        negative_float_inf = -float('inf')
        result = negative_float_inf
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= n:
                result = max(result, arr[mid])
            if arr[mid] > n:
                high = mid - 1
            else:
                low = mid + 1

        if result == negative_float_inf:
            return -1
        return result

    def binary_search_max(arr: list, n: int) -> int:
        float_inf = float('inf')
        result = float_inf
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= n:
                result = min(result, arr[mid])
            if arr[mid] > n:
                high = mid - 1
            else:
                low = mid + 1

        if result == float_inf:
            return -1
        return result

    values = []

    def rec(node: Optional[TreeNode]):
        if not node:
            return

        rec(node.left)
        values.append(node.val)
        rec(node.right)

    rec(root)
    result = []

    for i in queries:
        i_min = binary_search_min(values, i)
        i_max = binary_search_max(values, i)
        result.append([i_min, i_max])

    return result
