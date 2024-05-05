# my solution

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Node = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head: Node = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)

linked_list2 = LinkedList()
linked_list2.append(0)
linked_list2.append(2)
linked_list2.append(4)
linked_list2.append(5)
linked_list2.append(6)
linked_list2.append(777)
linked_list2.append(888)


def merge(lst1: LinkedList, lst2: LinkedList) -> LinkedList:
    result = LinkedList()
    cur: Node = None
    while all([lst1.head, lst2.head]):
        if lst1.head.data <= lst2.head.data:
            if result.head is None:
                result.head = lst1.head
                cur = result.head
            else:
                cur.next = lst1.head
                cur = cur.next
            lst1.head = lst1.head.next
        else:
            if result.head is None:
                result.head = lst2.head
                cur = result.head
            else:
                cur.next = lst2.head
                cur = cur.next
            lst2.head = lst2.head.next

    cur.next = lst1.head if lst1.head else lst2.head

    return result


merged = merge(linked_list, linked_list2)
print(merged)

# recursive solution:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)

linked_list2 = LinkedList()
linked_list2.append(0)
linked_list2.append(2)
linked_list2.append(4)
linked_list2.append(5)
linked_list2.append(6)
linked_list2.append(777)
linked_list2.append(888)


def merge_recursive(lst1: Node, lst2: Node) -> Node:
    if lst1 is None:
        return lst2
    elif lst2 is None:
        return lst1

    if lst1.data <= lst2.data:
        result = lst1
        result.next = merge_recursive(lst1.next, lst2)
    else:
        result = lst2
        result.next = merge_recursive(lst1, lst2.next)

    return result


def merge(lst1: LinkedList, lst2: LinkedList) -> LinkedList:
    result = LinkedList()
    result.head = merge_recursive(lst1.head, lst2.head)
    return result


merged = merge(linked_list, linked_list2)
print(merged)
