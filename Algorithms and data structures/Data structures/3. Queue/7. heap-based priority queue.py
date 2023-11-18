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

    priority_queue.push("Task 1", 9)
    priority_queue.push("Task 2", 8)
    priority_queue.push("Task 3", 7)
    priority_queue.push("Task 4", 6)
    priority_queue.push("Task 5", 5)
    priority_queue.push("Task 6", 4)
    priority_queue.push("Task 7", 3)
    priority_queue.push("Task 8", 2)
    priority_queue.push("Task 9", 1)

    while not priority_queue.is_empty():
        task = priority_queue.pop()
        print(f"Processed: {task}")

# Processed: Task 9
# Processed: Task 8
# Processed: Task 7
# Processed: Task 6
# Processed: Task 5
# Processed: Task 4
# Processed: Task 3
# Processed: Task 2
# Processed: Task 1
