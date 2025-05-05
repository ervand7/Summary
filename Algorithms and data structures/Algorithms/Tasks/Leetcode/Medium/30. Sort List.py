class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


# ChatGPT solution
def sort_list(head):
    if not head or not head.next:
        return head  # 0 or 1 node: already sorted

    # Step 1: Split list into two halves
    slow = head
    fast = head.next  # start fast one step ahead
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None  # break the list into two

    # Step 2: Sort both halves
    left = sort_list(head)
    right = sort_list(mid)

    # Step 3: Merge sorted halves
    return merge(left, right)


def merge(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the remaining part
    current.next = list1 if list1 else list2
    return dummy.next


def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


data = [4, 3, 2, 1]
head = build_linked_list(data)
res = sort_list(head)
print(res)
