# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    diameter = 0

    def longest_path(node):
        nonlocal diameter
        if not node:
            return 0
        left_path = longest_path(node.left)
        right_path = longest_path(node.right)
        diameter = max(diameter, left_path + right_path)
        return max(left_path, right_path) + 1

    longest_path(root)
    return diameter
