# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to find the intersection node.
def get_intersection_node(head_a, head_b):
    if not head_a or not head_b:
        return None

    pointer_a, pointer_b = head_a, head_b

    while pointer_a is not pointer_b:
        pointer_a = pointer_a.next if pointer_a else head_b
        pointer_b = pointer_b.next if pointer_b else head_a

    return pointer_a


# Creating the nodes for List A and List B
# List A: 1 -> 9 -> 1 -> 2 -> 4
a1 = ListNode(1)
a2 = ListNode(9)
a3 = ListNode(1)
a4 = ListNode(2)
a5 = ListNode(4)

# Linking nodes of List A
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

# List B: 3 -> 2 -> 4
b1 = ListNode(3)
# b2 and b3 will be intersection points (2 -> 4)
b2 = a4  # This is the intersection node
b3 = a5  # This is the next node after the intersection

# Linking nodes of List B
b1.next = b2
b2.next = b3

# Finding the intersection
intersection_node = get_intersection_node(a1, b1)
if intersection_node:
    print("Intersected at '" + str(intersection_node.val) + "'")
else:
    print("No intersection")
