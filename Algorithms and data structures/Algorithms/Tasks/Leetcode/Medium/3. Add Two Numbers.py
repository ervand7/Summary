# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# my solution
def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_values = []
    l2_values = []

    cur = l1
    while cur:
        l1_values.append(str(cur.val))
        cur = cur.next

    cur = l2
    while cur:
        l2_values.append(str(cur.val))
        cur = cur.next

    l1_number = int("".join(reversed(l1_values)))
    l2_number = int("".join(reversed(l2_values)))

    result_values = [int(i) for i in str(l1_number + l2_number)]
    result_values.reverse()
    head = ListNode(val=int(result_values[0]))
    cur = head
    for i in result_values[1:]:
        cur.next = ListNode(val=int(i))
        cur = cur.next

    return head
