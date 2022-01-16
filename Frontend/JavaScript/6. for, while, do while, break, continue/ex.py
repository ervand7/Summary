"""
В данном модуле представлены аналоги функций из ex1.js
но только на языке Python.
"""

# // while. Пример 2
s = 0
i = 1
while s < 100:
    s += i
    i += 1
print(s)  # 105


# // for. Пример 1
my_sum = 0
for i in range(1, 1000 + 1):
    my_sum += 1 / i
    i += 1
print(my_sum)  # 7.484470860550343


# // for. Пример 2
def lst_of_floats():
    n = 0
    lst = []
    while n <= 1:
        lst.append(round(n, 1))
        n += 0.1
    return lst


k, b = 0.5, 2
x = 0
for i in lst_of_floats():
    f = k * x + b
    x += 0.1
    print(f)
# 2.0
# 2.05
# 2.1
# 2.15
# 2.2
# 2.25
# 2.3
# 2.35
# 2.4
# 2.45
# 2.5
