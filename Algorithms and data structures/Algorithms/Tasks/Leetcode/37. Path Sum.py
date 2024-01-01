# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    flag = False
    if not root:
        return flag

    def rec(node: Optional[TreeNode], summa: int) -> None:
        nonlocal flag
        if not node.left and not node.right:
            if summa == target_sum:
                flag = True
            return

        if not node.left:
            return rec(node.right, summa + node.right.val)
        if not node.right:
            return rec(node.left, summa + node.left.val)

        rec(node.left, summa + node.left.val)
        rec(node.right, summa + node.right.val)

    rec(root, root.val)
    return flag


# ChatGPT solution
def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    # Check if it's a leaf node and if its value matches the target_sum
    if not root.left and not root.right:
        return root.val == target_sum

    # Subtract the current node's value from the target_sum
    target_sum -= root.val

    # Recursively check the left and right subtrees
    left_result = has_path_sum(root.left, target_sum)
    right_result = has_path_sum(root.right, target_sum)

    # Return True if there's a path with the target_sum in either subtree
    return left_result or right_result
