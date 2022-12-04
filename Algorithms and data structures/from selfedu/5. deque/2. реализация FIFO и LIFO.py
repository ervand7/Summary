from collections import deque

dq = deque([1, 2, 3, 4, 5])

# FIFO
dq.appendleft(10)
dq.pop()
# или
dq.append(10)
dq.popleft()

# LIFO
dq.append(10)
dq.pop()
# или
dq.appendleft(10)
dq.popleft()
