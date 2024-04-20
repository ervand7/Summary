# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    result = None

    def rec(node: Optional[TreeNode]) -> None:
        nonlocal result
        if node:
            if node.val == val:
                result = node
                return

            rec(node.left)
            rec(node.right)

    rec(root)
    return result


# ChatGPT iterative solution
def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    current = root
    while current:
        if current.val == val:
            return current
        elif current.val < val:
            current = current.right
        else:
            current = current.left
    return None
