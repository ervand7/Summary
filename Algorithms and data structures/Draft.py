# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        sub_values = []

        def rec_sub(node: Optional[TreeNode]):
            if node:
                sub_values.append(node.val)
                rec_sub(node.left)
                rec_sub(node.right)

        rec_sub(subRoot)
        # if len(sub_values) == 0:
        #     return True if not root else False

        a = None

        def rec_root(node: Optional[TreeNode]):
            nonlocal a
            if node:
                if node.val == sub_values[0]:
                    a = node
                    return
                else:
                    rec_root(node.left)
                    rec_root(node.right)

        rec_root(root)

        sub_values_from_root = []

        def rec_sub2(node: Optional[TreeNode]):
            if node:
                sub_values_from_root.append(node.val)
                rec_sub2(node.left)
                rec_sub2(node.right)

        rec_sub2(a)

        if len(sub_values) == 1:
            return set(sub_values) == set(sub_values_from_root)

        return sub_values == sub_values_from_root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(s: TreeNode, t: TreeNode) -> bool:
            if not s and not t:
                return True
            if s and t and s.val == t.val:
                return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
            return False

        if not subRoot:
            return True
        if not root:
            return False

        if isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
