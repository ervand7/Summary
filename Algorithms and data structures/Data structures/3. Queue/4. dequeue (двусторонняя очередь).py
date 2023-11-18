from collections import deque

# Create an empty deque
my_deque = deque()

# Append elements to the right side of the deque
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

# Append elements to the left side of the deque
my_deque.appendleft(0)

# Retrieve and remove elements from the right side of the deque
while my_deque:
    item = my_deque.pop()
    print("Popped from the right side:", item)

# Or retrieve and remove elements from the left side of the deque
while my_deque:
    item = my_deque.popleft()
    print("Popped from the left side:", item)

# Output:
# Popped from the right side: 3
# Popped from the right side: 2
# Popped from the right side: 1
# Popped from the right side: 0
