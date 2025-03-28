# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def sum_numbers(root: Optional[TreeNode]) -> int:
    def rec(node: Optional[TreeNode], current: int) -> int:
        if not node:
            return 0

        current = current * 10 + node.val
        if not node.left and not node.right:
            return current

        return rec(node.left, current) + rec(node.right, current)

    return rec(root, 0)
