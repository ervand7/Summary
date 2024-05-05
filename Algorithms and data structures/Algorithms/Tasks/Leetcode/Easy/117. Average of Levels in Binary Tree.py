# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My solution
def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    h = {}
    h_count = {}

    def rec(node: Optional[TreeNode], level) -> None:
        if not node:
            return

        if level not in h:
            h[level] = node.val
            h_count[level] = 1
        else:
            h[level] += node.val
            h_count[level] += 1

        rec(node.left, level + 1)
        rec(node.right, level + 1)

    rec(root, 0)

    return [v / h_count[k] for k, v in h.items()]
