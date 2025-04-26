from typing import Optional, List


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right


# ChatGPT solution
def balanceBST(root: TreeNode) -> TreeNode:
    def inorder(node: Optional[TreeNode]) -> List[int]:
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    def build(sorted_vals: List[int]) -> Optional[TreeNode]:
        if not sorted_vals:
            return None
        mid = len(sorted_vals) // 2
        node = TreeNode(sorted_vals[mid])
        node.left = build(sorted_vals[:mid])
        node.right = build(sorted_vals[mid + 1:])
        return node

    sorted_vals = inorder(root)
    return build(sorted_vals)
