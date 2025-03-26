# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def is_cousins(root: Optional[TreeNode], x: int, y: int) -> bool:
    distances = {
        x: 0,
        y: 0
    }
    node_parent = {
        x: 0,
        y: 0
    }

    def rec(node: Optional[TreeNode], parent_val: int, level: int) -> None:
        if node:
            val = node.val
            if val in {x, y}:
                distances[val] = level
                node_parent[val] = parent_val
                return
    
            rec(node.left, val, level + 1)
            rec(node.right, val, level + 1)

    rec(root, 0, 0)
    return distances[x] == distances[y] and node_parent[x] != node_parent[y]


# ChatGPT solution
def is_cousins(root: Optional[TreeNode], x: int, y: int) -> bool:
    queue = deque([(root, None)])  # (node, parent)

    while queue:
        len_queue = len(queue)
        x_parent = y_parent = None

        for _ in range(len_queue):
            node, parent = queue.popleft()

            if node.val == x:
                x_parent = parent
            if node.val == y:
                y_parent = parent

            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))

        # After processing one level
        if x_parent and y_parent:
            return x_parent != y_parent  # Same level, different parents
        if x_parent or y_parent:
            return False  # Found one but not the other → not same level

    return False
