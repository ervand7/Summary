from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def sum_of_left_leaves(root: Optional[TreeNode]) -> int:
    counter = 0

    def rec(node):
        if node is None:
            return

        nonlocal counter
        if node.left and node.left.left is None and node.left.right is None:
            counter += node.left.val
        rec(node.left)
        rec(node.right)

    rec(root)
    return counter
