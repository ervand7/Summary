# В этом примере append работает O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                if current.next is None:
                    self.tail = current
                return
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


if __name__ == "__main__":
    linked_list = LinkedList()
    for i in range(1, 10):
        linked_list.append(i)
    linked_list.prepend(0)
    linked_list.delete(2)
    linked_list.delete(7)
    linked_list.delete(9)

    print("Linked List:", linked_list.display())
