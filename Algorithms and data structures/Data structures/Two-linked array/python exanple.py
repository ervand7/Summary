class Node:

    def __init__(self, value=None, name=None):
        self.left = None
        self.right = None
        self.value = value
        self.name = name

    def __str__(self):
        return self.name


n1 = Node(1, name='n1')
n2 = Node(2, name='n2')
n3 = Node(3, name='n3')
n4 = Node(4, name='n4')

n2.left = n1
n2.right = n3

n3.left = n2
n3.right = n4

# for debug
a = 0
