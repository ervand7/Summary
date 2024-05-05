from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my recursive solution
def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def rec(node: Optional[TreeNode], r: list):
        if node:
            r.append(node.val)
            rec(node.left, r)
            rec(node.right, r)

    rec(root, result)
    return result


# iterative
def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so that left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
