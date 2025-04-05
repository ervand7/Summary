# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def evaluate_tree(root: Optional[TreeNode]) -> bool:
    def rec(node: Optional[TreeNode]) -> bool:
        if not node:
            return False

        if not node.left and not node.right:
            return True if node.val == 1 else False

        if node.val == 2:
            return rec(node.left) or rec(node.right)
        else:
            return rec(node.left) and rec(node.right)

    return rec(root)
