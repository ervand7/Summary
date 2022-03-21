# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    # make the head node
    node = head

    # loop through and delete duplicates by skipping them when seen
    while node and node.next:
        if node.val == node.next.val:
            node.next = node.next.next
        # we move along if no duplicate found
        else:
            node = node.next

    # return the head of the linked list
    return head


duplicate_three = ListNode(val=3, next=None)
three = ListNode(val=3, next=duplicate_three)
duplicate_two = ListNode(val=2, next=three)
two = ListNode(val=2, next=duplicate_two)
one = ListNode(val=1, next=two)

# for debug
result = deleteDuplicates(one)
b = 0
