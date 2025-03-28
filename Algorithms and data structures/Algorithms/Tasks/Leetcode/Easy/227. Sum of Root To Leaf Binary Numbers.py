# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ChatGPT solution
def sum_root_to_leaf(root: Optional[TreeNode]) -> int:
    def dfs(node, current):
        if not node:
            return 0

        # Build the number without bitwise ops
        current = current * 2 + node.val

        if not node.left and not node.right:
            return current

        return dfs(node.left, current) + dfs(node.right, current)

    return dfs(root, 0)
