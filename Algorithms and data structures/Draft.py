# def foo(item, lst=[]):
#     lst.append(item)
#     return lst
#
# print(foo(1))
# print(foo(2, []))
# print(foo(3, []))
# print(foo(4))


d = {"a": 1, "b": 2, "c": 3}

for k, v in d.items():
    if v == 3:
        v = 7

print(d)
