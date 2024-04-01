# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def find_target(root: Optional[TreeNode], k: int) -> bool:
    values = []

    def rec(node: Optional[TreeNode]) -> None:
        if node:
            values.append(node.val)
            rec(node.left)
            rec(node.right)

    rec(root)
    h = {}
    for i in values:
        if k - i in h:
            return True
        h[i] = True

    return False


# ChatGPT solution
def find_target(root, k):
    # Helper function to perform in-order traversal
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []

    # Perform in-order traversal to get elements in ascending order
    nums = inorder(root)

    # Use two-pointer technique to find if two numbers sum to k
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == k:
            return True
        elif current_sum < k:
            left += 1
        else:
            right -= 1

    return False
