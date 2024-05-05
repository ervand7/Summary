# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def find_second_minimum_value(root: Optional[TreeNode]) -> int:
    values = []

    def rec(node: Optional[TreeNode]) -> None:
        if node:
            values.append(node.val)
            rec(node.left)
            rec(node.right)

    rec(root)

    values = set(values)
    if len(values) in {0, 1}:
        return -1

    return sorted(list(values))[1]


# ChatGPT solution
def find_second_minimum_value(root: TreeNode) -> int:
    ans = float('inf')
    smallest = root.val

    def dfs(node):
        nonlocal ans
        if not node:
            return

        if smallest < node.val < ans:
            ans = node.val

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ans if ans < float('inf') else -1
