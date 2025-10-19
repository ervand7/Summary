# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ChatGPT solution
def construct_from_pre_post(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    if len(preorder) == 1:
        return root

    left_child_val = preorder[1]
    idx = postorder.index(left_child_val)
    left_size = idx + 1

    root.left = construct_from_pre_post(preorder[1:left_size + 1], postorder[:left_size])
    root.right = construct_from_pre_post(preorder[left_size + 1:], postorder[left_size:-1])

    return root


print(construct_from_pre_post(preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1]))
