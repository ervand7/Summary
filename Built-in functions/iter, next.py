# |||||||||||||||| iter и next ||||||||||||||||
m = iter('hi')
# print(next(m))
# print(next(m))

r = 'asd'
e = r.__iter__()
# print(e.__next__())
# print(e.__next__())
# print(e.__next__())

a = [43, 65, 3, 54, 6]
count = 0
# for i in a:
#     print(i + 5, a.index(i))
#     count += 1
#     print(f'{count}й обход')


# for i in range(len(a)):
#     print(i, a[i])

a1 = [1, 2, 34, 65, 87, 45, 0, 5, 5]
b = []
for i in a1:
    if not i in b:
        b.append(i)
# print(b)

a2 = [1, 2, 34, 65, 87, 45, 0, 5, 5]
# print(sorted(list(set(a2))))
