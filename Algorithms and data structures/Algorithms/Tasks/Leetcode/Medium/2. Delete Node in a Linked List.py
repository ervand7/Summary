# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# my solution
def delete_node(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    prev = None
    cur = node
    while cur.next:
        cur.val = cur.next.val
        prev = cur
        cur = cur.next

    prev.next = None


# ChatGPT solution
def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next
