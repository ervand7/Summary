from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4


# my best solution
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    result = None
    while head:
        temp = ListNode(head.val)
        if result is None:
            result = temp
        else:
            temp.next = result
            result = temp

        head = head.next

    return result


reverse_list(n1)
print()
# --------------------------------------------------------------------


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4


# my not best solution
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    values = []
    cur = head
    while cur is not None:
        values.append(cur.val)
        cur = cur.next

    cur = head
    for i in range(len(values) - 1, -1, -1):
        cur.val = values[i]
        cur = cur.next

    return head


reverse_list(n1)
print()
# --------------------------------------------------------------------


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


reverse_list(n1)
print()


# --------------------------------------------------------------------


# recursive
def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    def rec(node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return rec(n, node)

    return rec(head)


reverse_list(n1)
