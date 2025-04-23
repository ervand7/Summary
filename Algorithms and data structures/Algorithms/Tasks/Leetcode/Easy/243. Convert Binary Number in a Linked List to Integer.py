# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# my solution
def get_decimal_value(head: Optional[ListNode]) -> int:
    result = 0
    while head:
        result = result * 2 + head.val
        head = head.next

    return result
