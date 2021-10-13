def a():
    yield from 'oleg'


gen = a()
print(next(gen))  # o
print(next(gen))  # l
print(next(gen))  # e
print(next(gen))  # g
print(next(gen))  # StopIteration
