# |||||||||| lambda |||||||||||||||||
f = lambda x: x ** 2
print(f(7))  # 49

f = lambda x: 'positive' if x > 0 else 'negative'
print(f(123))  # positive

# сортировка по предпоследнему числу
a = [78, 56, 23, 8, 54512, 65, 98, 2354, 41, 5000]
a.sort(key=lambda x: x // 10 % 10)
print(a)  # [8, 5000, 54512, 23, 41, 56, 2354, 65, 78, 98]

# сортировка по длине
data = ["qwe", "q", "qw", "qeqwe", "r"]
print(sorted(data, key=lambda x: len(x)))  # ['q', 'r', 'qw', 'qwe', 'qeqwe']

# сортировка по четности
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sorted(a, key=lambda x: x % 2))  # [0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
