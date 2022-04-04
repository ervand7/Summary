from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4


# recursive
def reverseList1(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


# recursive
def reverseList2(head: Optional[ListNode]) -> Optional[ListNode]:
    def _reverse(node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return _reverse(n, node)

    return _reverse(head)


reverseList2(n1)
