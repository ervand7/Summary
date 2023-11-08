import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def pop(self):
        if not self.is_empty():
            return heapq.heappop(self.elements)[1]
        else:
            raise IndexError("Priority queue is empty")

    def is_empty(self):
        return len(self.elements) == 0


# Example usage:
if __name__ == "__main__":
    priority_queue = PriorityQueue()

    priority_queue.push("Task 1", 5)
    priority_queue.push("Task 2", 3)
    priority_queue.push("Task 3", 7)

    while not priority_queue.is_empty():
        task = priority_queue.pop()
        print(f"Processed: {task}")
