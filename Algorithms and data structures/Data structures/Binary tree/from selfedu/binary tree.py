from typing import Optional, Tuple


class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node: Node, parent: Optional[Node], value: int) \
            -> Tuple[Optional[Node], Optional[Node], bool]:
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(
                    node=node.left, parent=node, value=value
                )
        if value > node.data:
            if node.right:
                return self.__find(
                    node=node.right, parent=node, value=value
                )

        return node, parent, False

    def append(self, obj: Node):
        if self.root is None:
            self.root = obj
            return obj

        node, _, flag = self.__find(
            node=self.root, parent=None, value=obj.data
        )
        if flag is False and node:
            if obj.data < node.data:
                node.left = obj
            else:
                node.right = obj

        return obj

    def show_tree(self, node: Node):
        """ Алгоритм обхода в глубину """
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_wide_tree(self, node: Node):
        """ Алгоритм обхода в глубину """
        if node is None:
            return

        values = [node]
        while values:
            data = []
            for value in values:
                print(value.data, end=" ")
                if value.left:
                    data += [value.left]
                if value.right:
                    data += [value.right]

            print()
            values = data

    @staticmethod
    def __del_leaf(node: Node, parent: Node):
        if parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None

    @staticmethod
    def __del_one_child(node: Node, parent: Node):
        if parent.left == node:
            if node.left is None:
                parent.left = node.right
            elif node.right is None:
                parent.left = node.left

        elif parent.right == node:
            if node.left is None:
                parent.right = node.right
            elif node.right is None:
                parent.right = node.left

    def __find_min(self, node: Node, parent: Node) -> Tuple[Node, Node]:
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def del_node(self, key):
        node, parent, flag = self.__find(
            node=self.root, parent=None, value=key
        )
        if flag is False:
            return None

        if node.left is None and node.right is None:
            self.__del_leaf(node=node, parent=parent)
        elif node.left is None or node.right is None:
            self.__del_one_child(node=node, parent=parent)
        else:
            tree_min_val, parent_tree_min_val = \
                self.__find_min(node=node.right, parent=node)
            node.data = tree_min_val.data
            self.__del_one_child(
                node=tree_min_val, parent=parent_tree_min_val
            )


data = [10, 5, 7, 16, 13, 2, 20]
tree = Tree()
for i in data:
    tree.append(Node(i))
tree.show_tree(tree.root)
# 2
# 5
# 7
# 10
# 13
# 16
# 20

print()
tree.del_node(5)
tree.show_tree(tree.root)
# 2
# 7
# 10
# 13
# 16
# 20

print()
tree.show_wide_tree(tree.root)
# 10
# 7 16
# 2 13 20
