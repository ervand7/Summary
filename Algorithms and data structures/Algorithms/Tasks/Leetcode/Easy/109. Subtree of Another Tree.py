# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    def is_same_tree(t: TreeNode, s: TreeNode) -> bool:
        if not t and not s:
            return True
        if t and s and t.val == s.val:
            return is_same_tree(t.left, s.left) and is_same_tree(t.right, s.right)
        return False

    if not sub_root:
        return True
    if not root:
        return False

    if is_same_tree(root, sub_root):
        return True

    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)
