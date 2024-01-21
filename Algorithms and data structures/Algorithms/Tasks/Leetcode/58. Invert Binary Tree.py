from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)

    return root
