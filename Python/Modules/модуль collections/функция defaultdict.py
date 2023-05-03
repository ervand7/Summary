from collections import defaultdict

# благодаря defaultdict(int) у нас при обращении к несуществующим ключам будут автоматически
# создаваться эти ключи с дефолтным 0. А если у нас defaultdict(list), то дефолтом будет []
a = defaultdict(int)
print(a)  # defaultdict(<class 'int'>, {})
print(a['s'])  # 0
print(a)  # defaultdict(<class 'int'>, {'s': 0})

b = defaultdict(list)
print(b[1])  # []
print(b)  # defaultdict(<class 'list'>, {1: []})

print(a.default_factory)  # <class 'int'>
print(b.default_factory)  # <class 'list'>

# мы можем также переопределить дефолтные значения. Внимание! В атрибуте default_factory
# должно быть только callable значение
b.default_factory = lambda: [1, 2, 3]
print(b['Hello'])  # [1, 2, 3]
print(b)  # defaultdict(<function <lambda> at 0x7fb1a35ba1f0>, {1: [], 'Hello': [1, 2, 3]})

# находим сумму оценок
data = [
    ('ivanov', 2),
    ('petrov', 1),
    ('sidorov', 5),
    ('petrov', 3),
    ('ivanov', 2),
    ('ivanov', 4),
]
marks = defaultdict(int)
marks_list = defaultdict(list)
marks_unique = defaultdict(set)
for surname, mark in data:
    marks[surname] += mark
    marks_list[surname].append(mark)
    marks_unique[surname].add(mark)
print(marks)  # defaultdict(<class 'int'>, {'ivanov': 8, 'petrov': 4, 'sidorov': 5})
print(marks_list)  # defaultdict(<class 'list'>, {'ivanov': [2, 2, 4], 'petrov': [1, 3], 'sidorov': [5]})
print(marks_unique)  # defaultdict(<class 'set'>, {'ivanov': {2, 4}, 'petrov': {1, 3}, 'sidorov': {5}})
