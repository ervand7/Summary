from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'|{self.val}|'

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


# first decision
def isSameTree1(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p and q:
        return p.val == q.val \
               and isSameTree1(p.left, q.left) \
               and isSameTree1(p.right, q.right)
    return p == q


root = TreeNode(27)
[root.insert(i) for i in (14, 35, 10, 19, 31, 42)]

root2 = TreeNode(27)
[root2.insert(i) for i in (14, 35, 11, 19, 31, 42)]
print(isSameTree1(root, root2))


# second decision
def isSameTree2(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def t(n):
        return n and (n.val, t(n.left), t(n.right))

    return t(p) == t(q)


print(isSameTree2(root, root2))
