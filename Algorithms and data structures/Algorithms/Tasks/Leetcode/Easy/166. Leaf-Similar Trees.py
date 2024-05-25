# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def leaf_similar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    root1_leaves = []
    root2_leaves = []

    def get_leaves(node: TreeNode, arr: list) -> None:
        if node:
            if not node.left and not node.right:
                arr.append(node.val)
            else:
                get_leaves(node.left, arr)
                get_leaves(node.right, arr)

    get_leaves(root1, root1_leaves)
    get_leaves(root2, root2_leaves)

    return root1_leaves == root2_leaves


# ChatGPT solution
def leaf_similar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def get_leaf_values(root) -> list:
        leaves = []

        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return leaves

    return get_leaf_values(root1) == get_leaf_values(root2)
