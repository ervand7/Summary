from collections import deque

# deque - это двунаправленная очередь, которая очень быстро реализует
# добавление элементов в начало и конец очереди
d = deque()
d.append(1)
print(d)  # deque([1])
d.appendleft(2)
print(d)  # deque([2, 1])

# pop и popleft
my_deque = deque([1, 2, 3, 4, 5])
print(my_deque.pop())  # 5
print(my_deque.popleft())  # 5

# параметр maxlen. Принцип трубы и теннисных шариков
some = deque([1, 2, 3], maxlen=3)
print(some)  # deque([1, 2, 3], maxlen=3)
some.append(4)
print(some)  # deque([2, 3, 4], maxlen=3)
