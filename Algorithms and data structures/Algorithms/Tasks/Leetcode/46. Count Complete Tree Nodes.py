from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def count_nodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    result = 0

    def rec(node: Optional[TreeNode]):
        nonlocal result
        result += 1

        if node.left is not None:
            rec(node.left)
        if node.right is not None:
            rec(node.right)

    rec(root)
    return result


# ChatGPT solution
def count_nodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    def tree_depth(node):
        depth = 0
        while node.left:
            node = node.left
            depth += 1
        return depth

    def exists(idx, depth, node):
        left, right = 0, 2 ** depth - 1
        for _ in range(depth):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    depth = tree_depth(root)
    if depth == 0:
        return 1

    # Binary search to find the number of nodes in the last level
    left, right = 0, 2 ** depth - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if exists(pivot, depth, root):
            left = pivot + 1
        else:
            right = pivot - 1

    return (2 ** depth - 1) + left
