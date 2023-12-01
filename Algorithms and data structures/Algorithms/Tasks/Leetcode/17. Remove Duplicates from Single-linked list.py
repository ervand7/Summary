class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Node = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.last: Node = None

    def append(self, val: int) -> None:
        node = Node(val)
        if self.head is None:
            self.head = node
            self.last = self.head
        else:
            self.last.next = node
            self.last = self.last.next


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(1)
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(3)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)


def remove_duplicates(lst: LinkedList) -> None:
    hash_table = {}
    cur = lst.head
    prev = None
    while cur:
        if cur.val in hash_table:
            prev.next = cur.next
        else:
            hash_table[cur.val] = True
            prev = cur
        cur = cur.next


remove_duplicates(linked_list)
print()
