from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# recursive
def max_depth(root: Optional[TreeNode]) -> int:
    result = 0

    def rec(t: Optional[TreeNode], counter: int = 0) -> None:
        if t is None:
            return

        counter += 1
        nonlocal result
        if counter > result:
            result = counter

        rec(t.left, counter)
        rec(t.right, counter)

    rec(root)
    return result


# not my solution
def max_depth2(root: Optional[TreeNode]) -> int:
    def dfs(root, depth):
        if not root:
            return depth
        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

    return dfs(root, 0)


# iterative
def max_depth3(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = [(root, 1)]
    result = 0
    while stack:
        node, depth = stack.pop()
        if node:
            result = max(result, depth)
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

    return result
