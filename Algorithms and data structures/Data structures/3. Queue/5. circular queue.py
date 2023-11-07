class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.size = 0
        self.front = 0
        self.back = -1

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            # If the queue is full, overwrite the oldest element
            self.front = (self.front + 1) % self.capacity
        else:
            self.size += 1
        self.back = (self.back + 1) % self.capacity
        self.queue[self.back] = item

    def display(self):
        print(self.queue)


cq = CircularQueue(4)

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.display()  # [1, 2, 3, 4]

cq.enqueue(5)
cq.display()  # [5, 2, 3, 4]

cq.enqueue(6)
cq.display()  # [5, 6, 3, 4]

cq.enqueue(7)
cq.display()  # [5, 6, 7, 4]

cq.enqueue(8)
cq.display()  # [5, 6, 7, 8]

cq.enqueue(9)
cq.display()  # [9, 6, 7, 8]
