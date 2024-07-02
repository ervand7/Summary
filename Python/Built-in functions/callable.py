# ||||||||||||||| callable ||||||||||||||||||||
# функция callable показывает, является ди объект вызываемым
a = [1, 2, 3, 4, 5]
print(callable(a))  # False
print(callable(int))  # True
print(callable(type))  # True
