class TwoPriorityQueue:
    def __init__(self):
        self.high_priority = []  # High-priority queue
        self.low_priority = []  # Low-priority queue

    def push_high_priority(self, item):
        self.high_priority.append(item)

    def push_low_priority(self, item):
        self.low_priority.append(item)

    def pop_high_priority(self):
        if self.high_priority:
            return self.high_priority.pop(0)
        elif self.low_priority:
            return self.low_priority.pop(0)
        else:
            raise IndexError("Both priority queues are empty")

    def pop_low_priority(self):
        if self.low_priority:
            return self.low_priority.pop(0)
        elif self.high_priority:
            return self.high_priority.pop(0)
        else:
            raise IndexError("Both priority queues are empty")

    def is_empty(self):
        return not (self.high_priority or self.low_priority)


# Example usage:
if __name__ == "__main__":
    tpq = TwoPriorityQueue()

    tpq.push_high_priority("High-Priority Task 1")
    tpq.push_low_priority("Low-Priority Task 1")
    tpq.push_high_priority("High-Priority Task 2")
    tpq.push_low_priority("Low-Priority Task 2")

    while not tpq.is_empty():
        task = tpq.pop_high_priority() if tpq.high_priority else tpq.pop_low_priority()
        print(f"Processed: {task}")
