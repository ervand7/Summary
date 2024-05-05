from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def get_minimum_difference(root: Optional[TreeNode]) -> int:
    values = []

    def rec(node: Optional[TreeNode]) -> None:
        if node:
            values.append(node.val)
            rec(node.left)
            rec(node.right)

    rec(root)

    result = float("inf")
    values.sort()
    for i in range(1, len(values)):
        diff = values[i] - values[i - 1]
        if diff < result:
            result = diff

    return result
