class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return "Binary tree"

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def sorted_traversal(self):
        result = []
        self._sorted_traversal_recursive(self.root, result)
        return result

    def reversed_traversal(self):
        result = []
        self._reversal_traversal_recursive(self.root, result)
        return result

    def preorder_traversal(self):
        """ Left - right """
        result = []
        self._preorder_traversal_recursive(self.root, result)
        return result

    def postorder_traversal(self):
        """ Down up """
        result = []
        self._postorder_traversal_recursive(self.root, result)
        return result

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left:
                self._insert_recursive(current.left, value)
            else:
                current.left = Node(value)
        else:
            if current.right:
                self._insert_recursive(current.right, value)
            else:
                current.right = Node(value)

    def _search_recursive(self, current, value):
        if not current:
            return False
        if current.value == value:
            return True
        if value < current.value:
            return self._search_recursive(current.left, value)
        return self._search_recursive(current.right, value)

    def _sorted_traversal_recursive(self, node, result):
        if node:
            self._sorted_traversal_recursive(node.left, result)
            result.append(node.value)
            self._sorted_traversal_recursive(node.right, result)

    def _reversal_traversal_recursive(self, node, result):
        if node:
            self._reversal_traversal_recursive(node.right, result)
            result.append(node.value)
            self._reversal_traversal_recursive(node.left, result)

    def _preorder_traversal_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_traversal_recursive(node.left, result)
            self._preorder_traversal_recursive(node.right, result)

    def _postorder_traversal_recursive(self, node, result):
        if node:
            self._postorder_traversal_recursive(node.left, result)
            self._postorder_traversal_recursive(node.right, result)
            result.append(node.value)


"""
               10
         5             15
      3    7        13    17
"""

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(17)
tree.insert(13)

print("Sorted Traversal:", tree.sorted_traversal())  # [3, 5, 7, 10, 13, 15, 17]
print("Reversal inorder Traversal:", tree.reversed_traversal())  # [17, 15, 13, 10, 7, 5, 3]
print("Preorder Traversal:", tree.preorder_traversal())  # [10, 5, 3, 7, 15, 13, 17]
print("Postorder Traversal:", tree.postorder_traversal())  # [3, 7, 5, 13, 17, 15, 10]

print("Search for 7:", tree.search(7))  # True
print("Search for 12:", tree.search(12))  # False
