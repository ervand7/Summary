from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'== {self.val} =='


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])

    return root


a = sortedArrayToBST([-10, -3, 0, 5, 9])
# for debug
b = 0
