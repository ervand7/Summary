from collections import Counter

# подсчет кол-ва элементов в коллекции
s = 'abracadra'
letters = Counter(s)
print(letters)  # Counter({'a': 4, 'r': 2, 'b': 1, 'c': 1, 'd': 1})

words = ['Donald', 'Bob', 'Bob', 'Donald', 'Bob']
names = Counter(words)
print(names)  # Counter({'Bob': 3, 'Donald': 2})

# метод elements выводит повторяющиеся рядом друг с другом
names_list = [n for n in names.elements()]
print(names_list)  # ['Donald', 'Donald', 'Bob', 'Bob', 'Bob']

# метод most_common выводит значения от самых часто повторяющихся до самых редких
print(names.most_common())  # [('Bob', 3), ('Donald', 2)]
print(letters.most_common())  # [('a', 4), ('r', 2), ('b', 1), ('c', 1), ('d', 1)]
# он также может принимать в себя аргумент - кол-во выводимых элементов
print(letters.most_common(2))  # [('a', 4), ('r', 2)]

# передав в Counter несуществующий ключ мы не получим ошибку, а получим 0
print(letters['z'])  # gives 0 instead of error
my_counter = Counter()
for i in [1, 1, 1, 2, 2, 3, 3, 3, 3]:
    my_counter[i] += 1
print(my_counter)  # Counter({3: 4, 1: 3, 2: 2})

#  можно складывать 2 Counter'а. Сложение будет идти по ключам
another_counter = Counter([2, 2, 2, 3, 3, 4, 4, 4, 4, 4])
print(my_counter + another_counter)  # Counter({3: 6, 2: 5, 4: 5, 1: 3})

#  можно также вычитать один счетчик из другого
print(another_counter - my_counter)  # Counter({4: 5, 2: 1})
