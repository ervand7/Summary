# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def largest_values(root: Optional[TreeNode]) -> List[int]:
    h = {}
    minimum_value = -float('inf')

    def rec(node: Optional[TreeNode], level: int):
        if not node:
            return

        h[level] = max(h.get(level, minimum_value), node.val)
        rec(node.left, level + 1)
        rec(node.right, level + 1)

    rec(root, 0)
    return list(h.values())
