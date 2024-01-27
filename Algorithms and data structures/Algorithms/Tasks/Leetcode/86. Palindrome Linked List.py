from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# my solution
def is_palindrome(head: Optional[ListNode]) -> bool:
    data = []
    while head:
        data.append(head.val)
        head = head.next

    for i in range(len(data) // 2):
        if data[i] != data[len(data) - 1 - i]:
            return False

    return True
