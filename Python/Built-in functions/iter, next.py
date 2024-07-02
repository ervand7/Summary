# |||||||||||||||| iter и next ||||||||||||||||
a = iter('hi')
print(next(a))  # h
print(next(a))  # i

a = 'asd'
a = a.__iter__()
print(a.__next__())  # a
print(a.__next__())  # s
print(a.__next__())  # d
