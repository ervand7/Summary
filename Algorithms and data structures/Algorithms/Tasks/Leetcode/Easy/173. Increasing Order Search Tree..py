# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# my solution
def increasing_bst(root: TreeNode) -> TreeNode:
    result, pointer = None, None

    def sorted_traverse(node: TreeNode) -> None:
        nonlocal result
        nonlocal pointer

        if node:
            sorted_traverse(node.left)
            if not result:
                result = TreeNode(node.val)
                pointer = result
            else:
                result.right = TreeNode(node.val)
                result = result.right
            sorted_traverse(node.right)

    sorted_traverse(root)

    return pointer
