# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def find_mode(root: Optional[TreeNode]) -> List[int]:
    result = {}

    def rec(node: Optional[TreeNode], h: dict) -> None:
        if node:
            h[node.val] = h.get(node.val, 0) + 1
            rec(node.left, h)
            rec(node.right, h)

    rec(root, result)

    s = sorted(result.items(), key=lambda x: x[1], reverse=True)
    maximum = s[0][1]
    r = []
    for k, v in s:
        if v == maximum:
            r.append(k)
        else:
            break
    return r
