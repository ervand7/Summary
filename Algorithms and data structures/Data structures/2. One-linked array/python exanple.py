class ListNode:
    def __init__(self, val=0, next=None, name=None):
        self.val = val
        self.next = next
        self.name = name

    def __str__(self):
        return self.name


n1 = ListNode(1, name='n1')
n2 = ListNode(2, name='n2')
n3 = ListNode(3, name='n3')
n4 = ListNode(4, name='n4')

n1.next = n2
n2.next = n3
n3.next = n4

# for debug
a = 0
