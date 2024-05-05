# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# my solution
def preorder(root: 'Node') -> List[int]:
    if not root:
        return []

    values = []

    def rec(node: 'Node') -> None:
        values.append(node.val)
        if node.children is not None:
            for i in node.children:
                rec(i)

    rec(root)
    return values


# chatGPT iterative solution
def preorder_iterative(node):
    if not node:
        return []

    result = []
    stack = [node]

    while stack:
        current = stack.pop()
        result.append(current.val)
        # Reverse to maintain the left-to-right order
        stack.extend(reversed(current.children))

    return result
