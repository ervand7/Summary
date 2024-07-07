# A metaclass is a special purpose class that generates classes

print(type(int))  # <class 'type'>
print(type(str))  # <class 'type'>
print(type(dict))  # <class 'type'>
print(type(set))  # <class 'type'>
print(type(tuple))  # <class 'type'>
print(type(list))  # <class 'type'>
print(type(object))  # <class 'type'>
print(type(type))  # <class 'type'>


class A: pass
print(type(A))  # <class 'type'>
