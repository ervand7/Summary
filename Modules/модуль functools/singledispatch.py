# https://www.geeksforgeeks.org/function-overloading-with-singledispatch-functools/
from functools import singledispatch


@singledispatch
def fun(s):
    print(s)


@fun.register(int)
def _1(s):
    print(s * 2)


@fun.register(list)
def _2(s):
    for i, e in enumerate(s): print(i, e)


fun('GeeksforGeeks')  # GeeksforGeeks
fun(10)  # 20
fun(['g', 'e', 'e', 'k', 's'])
# 0 g
# 1 e
# 2 e
# 3 k
# 4 s
