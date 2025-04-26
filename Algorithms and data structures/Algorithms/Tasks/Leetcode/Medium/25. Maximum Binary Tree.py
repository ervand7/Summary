# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def construct_maximum_binary_tree(nums: List[int]) -> Optional[TreeNode]:
    def rec(node: Optional[TreeNode], sub: List[int]):
        idx = sub.index(node.val)
        left_values = sub[:idx]
        right_values = sub[idx + 1:]
        if left_values:
            node.left = TreeNode(val=max(left_values))
            rec(node.left, left_values)
        if right_values:
            node.right = TreeNode(val=max(right_values))
            rec(node.right, right_values)

    node = TreeNode(val=max(nums))
    rec(node, nums)
    return node
