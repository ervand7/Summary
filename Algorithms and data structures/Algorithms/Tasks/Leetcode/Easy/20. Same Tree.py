from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)

        else:
            self.val = val


class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)


a = TreeNode()
b = TreeNode()
for i in range(10):
    a.insert(i)
    b.insert(i)

print(Solution().is_same_tree(a, b))  # True

a.insert(55)
print(Solution().is_same_tree(a, b))  # False
