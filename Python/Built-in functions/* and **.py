# https://stackoverflow.com/questions/21809112/what-does-tuple-and-dict-mean-in-python#answers

# -------------------------------- In a function call --------------------------------
#  ============= OPERATOR <*> =============
def foo(x, y):
    print(x, y)


t = (1, 2)
foo(*t)

# Since v3.5, you can also do this in a list/tuple/set literals:
print([1, *(2, 3), 4])  # [1, 2, 3, 4]


# ============= OPERATOR <**> =============

def foo2(x, y):
    print(x, y)


d = {'x': 1, 'y': 2}
foo2(**d)  # 1 2

# Since v3.5, you can also do this in a dictionary literals:
d = {'a': 1}
print({'b': 2, **d})  # {'b': 2, 'a': 1}


# -------------------------------- In a function signature --------------------------------

#  ============= OPERATOR <*> =============
def foo(*tup):
    print(tup)


foo(1, 2)  # (1, 2)


# ============= OPERATOR <**> =============
def foo(**dct):
    print(dct)


foo(x=1, y=2)  # {'y': 2, 'x': 1}

# -------------------------------- In assignments and for loops --------------------------------


#  ============= OPERATOR <*> =============
x, *xs = (1, 2, 3, 4)
print(x)  # 1
print(xs)  # [2, 3, 4]

*xs, x = (1, 2, 3, 4)
print(xs)  # [1, 2, 3]
print(x)  # 4

x, *xs, y = (1, 2, 3, 4)
print(x)  # 1
print(xs)  # [2, 3]
print(y)  # 4

for x, *y, z in [(1, 2, 3, 4)]: print(x, y, z)  # 1 [2, 3] 4


# !!! Note that parameters that appear after a * are keyword-only !!!
def f(a, *, b): ...


# f(1, b=2)  # fine
# f(1, 2)  # error: b is keyword-only


# !!! Python3.8 added positional-only parameters, meaning parameters that cannot be
# used as keyword arguments. They are appear before a / (a pun on * preceding keyword-only args).

def fun(a, /, p, *, k): ...
# fun(1, 2, k=3)  # fine
# fun(1, p=2, k=3)  # fine
# fun(a=1, p=2, k=3)  # error: a is positional-only
