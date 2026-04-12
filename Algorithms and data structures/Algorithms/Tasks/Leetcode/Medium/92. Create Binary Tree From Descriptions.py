from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.val}"


# my solution
# Time: O(n)
# Space: O(n)
def create_binary_tree(descriptions: List[List[int]]) -> Optional[TreeNode]:
    h = {}
    child_parent = {}

    first = True
    for parent, child, is_left in descriptions:
        if first:
            first = False
            parent_node = TreeNode(val=parent)
            child_node = TreeNode(val=child)
            if is_left == 1:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            h[parent] = parent_node
            h[child] = child_node

            child_parent[child] = parent
            child_parent[parent] = None

        else:
            if parent in h:
                if child in h:
                    child_node = h.get(child)
                else:
                    child_node = TreeNode(val=child)
                    h[child] = child_node

                if is_left == 1:
                    h[parent].left = child_node
                else:
                    h[parent].right = child_node
            else:
                if child in h:
                    child_node = h.get(child)
                else:
                    child_node = TreeNode(val=child)
                    h[child] = child_node

                parent_node = TreeNode(val=parent)
                h[parent] = parent_node

                if is_left == 1:
                    parent_node.left = child_node
                else:
                    parent_node.right = child_node

            child_parent[child] = parent

    # take any current
    while True:
        if child_parent.get(child) is None:
            result = h.get(child)
            return result
        child = child_parent[child]


# refined version
def create_binary_tree(descriptions: List[List[int]]) -> Optional[TreeNode]:
    nodes = {}
    children = set()

    for parent, child, is_left in descriptions:
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child)

        if is_left == 1:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]

        children.add(child)

    for parent, _, _ in descriptions:
        if parent not in children:
            return nodes[parent]


# ChatGPT solution
# Time: O(n)
# Space: O(n)
def create_binary_tree(descriptions: List[List[int]]) -> Optional[TreeNode]:
    nodes = {}
    children = set()

    for parent, child, is_left in descriptions:
        if parent not in nodes:
            nodes[parent] = TreeNode(parent)
        if child not in nodes:
            nodes[child] = TreeNode(child)

        if is_left == 1:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]

        children.add(child)

    for parent, _, _ in descriptions:
        if parent not in children:
            return nodes[parent]


print(create_binary_tree(descriptions=[[85, 82, 1], [74, 85, 1], [39, 70, 0], [82, 38, 1], [74, 39, 0], [39, 13, 1]]))

#             74
#        85               39
#    82               13      70
# 38
#
