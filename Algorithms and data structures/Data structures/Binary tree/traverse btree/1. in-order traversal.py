class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __str__(self):
        return f'|{self.data}|'

    def insert(self, data):
        """Recursive insert"""
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    def PrintTree(self):
        """Recursive print"""
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)


# for debug
a = root
print(root.inorderTraversal(root))


def inorderTraversal1(root):
    res = []
    helper(root, res)
    return res


def helper(root, res):
    if root:
        helper(root.left, res)
        res.append(root.data)
        helper(root.right, res)


"""
                       27
           14                      35
      10        19             31     42

"""

print(inorderTraversal1(root))
