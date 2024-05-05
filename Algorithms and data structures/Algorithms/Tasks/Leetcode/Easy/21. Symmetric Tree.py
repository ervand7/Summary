from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursively
class Solution:
    def is_symmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and is_mirror(t1.right, t2.left) and is_mirror(t1.left, t2.right)

        return is_mirror(root, root)


# iteratively
class Solution2:
    def is_symmetric(self, root):
        if not root:
            return True

        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()

            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False

            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True
