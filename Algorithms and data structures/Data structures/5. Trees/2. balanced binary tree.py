class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self):
        self.root = None

    @staticmethod
    def get_height(node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, node):
        right = node.right
        right_left = right.left

        right.left = node
        node.right = right_left

        self.update_height(node)
        self.update_height(right)

        return right

    def rotate_right(self, node):
        left = node.left
        left_right = left.right

        left.right = node
        node.left = left_right

        self.update_height(node)
        self.update_height(left)

        return left

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(root.value)
            result += self.inorder_traversal(root.right)
        return result

    def display(self):
        result = self.inorder_traversal(self.root)
        return result

    def _insert_recursive(self, root, value):
        if not root:
            return Node(value)

        if value < root.value:
            root.left = self._insert_recursive(root.left, value)
        else:
            root.right = self._insert_recursive(root.right, value)

        self.update_height(root)
        balance = self.get_balance(root)

        if balance > 1:
            if value < root.left.value:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if value > root.right.value:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root


tree = Tree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)

print(tree.display())
#               4
#     2                   6
# 1       3           5        7
