from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my recursive solution
def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def rec(node: Optional[TreeNode], r: list) -> None:
        if node:
            rec(node.left, r)
            rec(node.right, r)
            r.append(node.val)

    rec(root, result)
    return result


# iterative
def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []

    stack1, stack2, output = [root], [], []

    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        output.append(node.val)

    return output

