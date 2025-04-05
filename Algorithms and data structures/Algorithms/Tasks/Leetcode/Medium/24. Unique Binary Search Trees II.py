# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ChatGPT solution
def generate_trees(n: int) -> List[Optional[TreeNode]]:
    if n == 0:
        return []

    def build_trees(start, end) -> List[Optional[TreeNode]]:
        trees = []
        if start > end:
            return [None]
        for i in range(start, end + 1):
            left_subtrees = build_trees(start, i - 1)
            right_subtrees = build_trees(i + 1, end)
            for left in left_subtrees:
                for right in right_subtrees:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    trees.append(root)
        return trees

    return build_trees(1, n)


a = generate_trees(3)
print(a)
