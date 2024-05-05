from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive
def min_depth(root: Optional[TreeNode]):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if not root.left:
        return min_depth(root.right) + 1
    if not root.right:
        return min_depth(root.left) + 1
    return min(min_depth(root.left), min_depth(root.right)) + 1


# iterative
def min_depth2(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = [(root, 1)]
    while stack:
        node, depth = stack.pop(0)
        if not node.left and not node.right:
            return depth
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
