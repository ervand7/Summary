from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    prev, current = dummy, head

    while current:
        if current.val == val:
            # Remove the current node
            prev.next = current.next
        else:
            # Move prev to current if current node is not deleted
            prev = current
        # Move to the next node
        current = current.next

    # Return the new head of the list, which is the next of dummy node
    return dummy.next
