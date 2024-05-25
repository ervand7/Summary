# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# my solution
def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    data = {}
    i = 0
    while head:
        data[i] = head
        head = head.next
        i += 1

    return data[len(data) // 2]


# ChatGPT solution
def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
