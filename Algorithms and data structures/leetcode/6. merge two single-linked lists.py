# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) \
        -> Optional[ListNode]:
    cur = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1, cur = list1.next, list1
        else:
            cur.next = list2
            list2, cur = list2.next, list2

    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next


one = ListNode(val=1)
two = ListNode(val=2)

mergeTwoLists(one, two)
# debug
a = one
b = two
c = 0


# ______________________________________________________________
def recursive_solution(list1, list2):
    if None in (list1, list2):
        return list1 or list2

    if list1.val < list2.val and list1:
        list1.next = recursive_solution(list1.next, list2)
        return list1
    else:
        list2.next = recursive_solution(list1, list2.next)
        return list2


second_one = ListNode(val=1)
second_two = ListNode(val=2)

recursive_solution(second_one, second_two)
# debug
x = second_one
y = second_two
d = 0
