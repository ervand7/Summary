# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def range_sum_BST(root: Optional[TreeNode], low: int, high: int) -> int:
    result = 0

    def rec(node: Optional[TreeNode]) -> None:
        nonlocal result
        if node:
            if low <= node.val <= high:
                result += node.val
            rec(node.left)
            rec(node.right)

    rec(root)
    return result
