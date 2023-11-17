from collections import deque

dq = deque()
print(dq)  # deque([])

dq = deque([1, 2, 3, 4, 5], maxlen=5)
print(dq)  # deque([1, 2, 3, 4, 5], maxlen=5)

dq.append(6)
print(dq)  # deque([2, 3, 4, 5, 6], maxlen=5)

dq = deque([1, 2, 3, 4, 5], maxlen=5)
dq.appendleft(6)
print(dq)  # deque([6, 1, 2, 3, 4], maxlen=5)

dq = deque([1, 2, 3, 4, 5])
dq.append(6)
print(dq)  # deque([1, 2, 3, 4, 5, 6])

dq = deque([1, 2, 3, 4, 5])
dq.pop()
print(dq)  # deque([1, 2, 3, 4])

dq = deque([1, 2, 3, 4, 5])
dq.popleft()
print(dq)  # deque([2, 3, 4, 5])

dq = deque([1, 2, 3, 4, 5])
dq.extend([6, 7, 8])
print(dq)  # deque([1, 2, 3, 4, 5, 6, 7, 8])

dq = deque([1, 2, 3, 4, 5])
dq.extendleft([6, 7, 8])
print(dq)  # deque([8, 7, 6, 1, 2, 3, 4, 5])

dq = deque([1, 2, 3, 4, 5])
dq.insert(1, 100)
print(dq)  # deque([1, 100, 2, 3, 4, 5])

dq = deque([1, 2, 3, 4, 5, 3])
dq.remove(3)
print(dq)  # deque([1, 2, 4, 5, 3])

dq = deque([1, 2, 3, 4, 5])
dq.clear()
print(dq)  # deque([])

dq = deque([1, 2, 3, 4, 5])
dq2 = dq.copy()
print(dq2)  # deque([1, 2, 3, 4, 5])
