# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def smallest_from_leaf(root: Optional[TreeNode]) -> str:
    words = []
    alphabet = {
        0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i',
        9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q',
        17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y',
        25: 'z'
    }

    def rec(node: Optional[TreeNode], path: str):
        if not node:
            return

        path += alphabet[node.val]
        if not node.left and not node.right:
            words.append(path[::-1])

        rec(node.left, path)
        rec(node.right, path)

    rec(root, "")
    return min(words)
