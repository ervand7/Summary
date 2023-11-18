import queue

# Create an empty priority queue
my_priority_queue = queue.PriorityQueue()

# Add elements with associated priorities to the queue
my_priority_queue.put((3, "Task C"))
my_priority_queue.put((1, "Task A"))
my_priority_queue.put((2, "Task B"))

# Retrieve elements from the priority queue based on their priorities
while not my_priority_queue.empty():
    priority, task = my_priority_queue.get()
    print(f"Task '{task}' with priority {priority} is processed.")

# Output:
# Task 'Task A' with priority 1 is processed.
# Task 'Task B' with priority 2 is processed.
# Task 'Task C' with priority 3 is processed.
