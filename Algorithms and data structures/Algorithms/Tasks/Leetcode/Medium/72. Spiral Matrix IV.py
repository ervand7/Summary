from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


values = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
head = build_linked_list(values)


def spiral_matrix(m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    matrix = [[-1] * n for _ in range(m)]

    top, bottom = 0, m - 1
    left, right = 0, n - 1

    while head and top <= bottom and left <= right:

        # left → right
        for col in range(left, right + 1):
            if not head:
                return matrix
            matrix[top][col] = head.val
            head = head.next
        top += 1

        # top → bottom
        for row in range(top, bottom + 1):
            if not head:
                return matrix
            matrix[row][right] = head.val
            head = head.next
        right -= 1

        # right → left
        if top <= bottom:
            for col in range(right, left - 1, -1):
                if not head:
                    return matrix
                matrix[bottom][col] = head.val
                head = head.next
            bottom -= 1

        # bottom → top
        if left <= right:
            for row in range(bottom, top - 1, -1):
                if not head:
                    return matrix
                matrix[row][left] = head.val
                head = head.next
            left += 1

    return matrix


for i in (spiral_matrix(m=3, n=5, head=head)):
    print(i)
