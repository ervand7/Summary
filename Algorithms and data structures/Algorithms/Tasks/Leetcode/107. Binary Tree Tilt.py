# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def find_tilt(root: Optional[TreeNode]) -> int:
    values = []

    def rec(node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        left_val = rec(node.left)
        right_val = rec(node.right)

        values.append(abs(left_val - right_val))
        return node.val + left_val + right_val

    rec(root)
    return sum(values)
