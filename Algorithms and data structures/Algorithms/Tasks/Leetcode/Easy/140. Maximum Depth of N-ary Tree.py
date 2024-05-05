# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# my solution
def max_depth(root: 'Node') -> int:
    if not root:
        return 0

    count = 0

    def rec(node: 'Node', level: int) -> None:
        nonlocal count
        count = max(count, level)
        if node.children is not None:
            for i in node.children:
                rec(i, level + 1)

    rec(root, 1)
    return count
