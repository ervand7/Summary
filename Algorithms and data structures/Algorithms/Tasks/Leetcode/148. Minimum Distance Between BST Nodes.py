# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
# Here we use sorted traversal recursive
def min_diff_in_bst(root: Optional[TreeNode]) -> int:
    values = []

    def rec(node: Optional[TreeNode]) -> None:
        if node:
            rec(node.left)
            values.append(node.val)
            rec(node.right)

    rec(root)

    result = float("inf")
    for i in range(1, len(values)):
        diff = values[i] - values[i - 1]
        result = min(result, diff)

    return result


# ChatGPT solution
# Смысл: так как дерево BST, то изначально воспринимаем его как отсортированный список
# 1) находим самое левое (и по факту - минимальное) значение. И далее
# по лесенке идем вверх
# 2) найденное значение уже сравниваем с любым другим значением узлов
def min_diff_in_bst(root: Optional[TreeNode]) -> int:
    prev = None
    min_diff = float('inf')

    def inorder(node):
        nonlocal prev, min_diff
        if not node:
            return

        inorder(node.left)

        if prev is not None:
            min_diff = min(min_diff, node.val - prev)
        prev = node.val

        inorder(node.right)

    inorder(root)
    return min_diff


root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
min_diff_in_bst(root1)
