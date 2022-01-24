from collections import ChainMap

# ChainMap нужен для логического объединения словарей
first = {1: 1, 2: 2, 3: 3}
second = {4: 4, 5: 5, 6: 6}
chain = ChainMap(first, second)
print(chain)  # ChainMap({1: 1, 2: 2, 3: 3}, {4: 4, 5: 5, 6: 6})
print(1 in chain)  # True
print(5 in chain)  # True
