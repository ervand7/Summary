from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    visited = set()
    cur = head

    while cur:
        if cur in visited:
            return cur
        visited.add(cur)
        cur = cur.next

    return None


a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

a.next = b
b.next = c
c.next = d
d.next = b

print()

print(detect_cycle(a))
