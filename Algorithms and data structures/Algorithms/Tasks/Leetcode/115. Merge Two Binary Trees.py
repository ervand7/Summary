# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def merge_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1:
        return root2
    if not root2:
        return root1

    def rec(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> None:
        if root1 and root2:
            root1.val += root2.val
            if all([root1.left, root2.left]):
                rec(root1.left, root2.left)
            if all([root1.right, root2.right]):
                rec(root1.right, root2.right)

            if root2.left and not root1.left:
                root1.left = root2.left

            if root2.right and not root1.right:
                root1.right = root2.right

    rec(root1, root2)
    return root1


# ChatGPT solution
def merge_trees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root1:
        return root2
    if not root2:
        return root1

    root1.val += root2.val
    root1.left = merge_trees(root1.left, root2.left)
    root1.right = merge_trees(root1.right, root2.right)

    return root1
