def f(x=list()):
    x.append(1)
    return x


print(f(), f(), f())  # [1, 1, 1] [1, 1, 1] [1, 1, 1]


def f(x=list()):
    x.append(1)
    return x


a = print(f()), print(f()), print(f())
# [1]
# [1, 1]
# [1, 1, 1]

