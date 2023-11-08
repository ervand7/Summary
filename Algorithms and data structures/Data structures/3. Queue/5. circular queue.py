class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.pointer = 0

    def enqueue(self, item):
        self.queue[self.pointer] = item
        self.pointer = (self.pointer + 1) % self.capacity

    def display(self):
        print(self.queue)


cq = CircularQueue(5)

for i in range(20):
    cq.enqueue(i)
    cq.display()

# [0, None, None, None, None]
# [0, 1, None, None, None]
# [0, 1, 2, None, None]
# [0, 1, 2, 3, None]
# [0, 1, 2, 3, 4]
# [5, 1, 2, 3, 4]
# [5, 6, 2, 3, 4]
# [5, 6, 7, 3, 4]
# [5, 6, 7, 8, 4]
# [5, 6, 7, 8, 9]
# [10, 6, 7, 8, 9]
# [10, 11, 7, 8, 9]
# [10, 11, 12, 8, 9]
# [10, 11, 12, 13, 9]
# [10, 11, 12, 13, 14]
# [15, 11, 12, 13, 14]
# [15, 16, 12, 13, 14]
# [15, 16, 17, 13, 14]
# [15, 16, 17, 18, 14]
# [15, 16, 17, 18, 19]
