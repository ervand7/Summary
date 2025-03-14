def add(a, b):
    return a + b


def decorator(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'function "{func.__name__}" was called {count} times')
        return func(*args, **kwargs)

    return inner


d = decorator(add)
d(1, 2)  # function "add" was called 1 times
d(1, 2)  # function "add" was called 2 times
d(1, 2)  # function "add" was called 3 times
