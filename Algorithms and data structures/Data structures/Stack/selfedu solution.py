from collections import deque

stack = deque()
stack.append(4)
stack.append(5)
print(stack)  # deque([4, 5])
print(stack.pop())  # 5
print(stack.pop())  # 4

# или
stack = deque()
stack.appendleft(4)
stack.appendleft(5)
print(stack)  # deque([5, 4])
print(stack.popleft())  # 5
print(stack.popleft())  # 4

