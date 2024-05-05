# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# my solution
def postorder(root: 'Node') -> List[int]:
    if not root:
        return []

    values = []

    def rec(node: 'Node') -> None:
        if node.children is not None:
            for i in node.children:
                rec(i)
            values.append(node.val)

    rec(root)
    return values


# ChatGPT iterative solution
def postorder_iterative(node):
    if not node:
        return []

    result = []
    stack = [node]

    while stack:
        current = stack.pop()
        result.append(current.val)
        stack.extend(current.children)

    return result[::-1]
