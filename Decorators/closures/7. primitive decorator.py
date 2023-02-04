def add(a, b):
    return a + b


def decorator(above_written_func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'function "{above_written_func.__name__}" was called {count} times')
        return above_written_func(*args, **kwargs)

    return inner


d = decorator(add)
print(d(1, 2))
print(d(1, 2))
print(d(1, 2))

# function "add" was called 1 times
# 3
# function "add" was called 2 times
# 3
# function "add" was called 3 times
# 3
