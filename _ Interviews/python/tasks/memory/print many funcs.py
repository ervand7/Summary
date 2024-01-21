def f(x=[]):
    x.append(1)
    return x


print(f(), f(), f())  # [1, 1, 1] [1, 1, 1] [1, 1, 1]
