from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    result = []

    if not root:
        return result

    def rec(node: Optional[TreeNode], path: str):
        if not node:
            return

        path = f"{path}->{node.val}"
        if not node.left and not node.right:
            result.append(path)
            return

        rec(node.left, path)
        rec(node.right, path)

    if not root.left and not root.right:
        result.append(str(root.val))
        return result

    rec(root.left, str(root.val))
    rec(root.right, str(root.val))
    return result


# ChatGPT solution
def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    if not root:
        return []

    paths = []

    def dfs(node, path):
        if not node.left and not node.right:  # Leaf node
            paths.append(path + str(node.val))
            return

        if node.left:
            dfs(node.left, path + str(node.val) + "->")

        if node.right:
            dfs(node.right, path + str(node.val) + "->")

    dfs(root, "")
    return paths
