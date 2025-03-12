# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def is_unival_tree(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    val = root.val
    result = True

    def rec(node: Optional[TreeNode]) -> None:
        nonlocal val
        nonlocal result

        if node:
            if node.val != val:
                result = False
                return
            rec(node.left)
            rec(node.right)

    rec(root)
    return result


# ChatGPT iterative solution
def is_unival_tree(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    # Use a stack for DFS traversal.
    stack = [root]
    while stack:
        node = stack.pop()
        # If the current node's value doesn't match the root's value, return False.
        if node.val != root.val:
            return False
        # Add children to the stack if they exist.
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return True  # All nodes matched the root's value.


# ChatGPT recursive solution
def is_unival_tree(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    # Recursively check if left and right subtrees are univalued and match the root's value.
    if root.left and root.left.val != root.val:
        return False
    if root.right and root.right.val != root.val:
        return False

    return is_unival_tree(root.left) and is_unival_tree(root.right)
