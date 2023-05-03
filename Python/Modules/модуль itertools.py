# основная статья: https://pythonworld.ru/moduli/modul-itertools.html
import itertools

# itertools.count(start=0, step=1) - бесконечная арифметическая прогрессия с первым членом start и шагом step
iterator_count = itertools.count(start=0, step=5)
for i in iterator_count:
    if i == 25:
        break
    print(i, end=' ')  # 0 5 10 15 20

# itertools.cycle(iterable) - возвращает по одному значению из последовательности, повторенной бесконечное число раз
iterator_cycle = itertools.cycle([1, 2, 3, 4, 234, 456, 678, 534])
for i in iterator_cycle:
    if i == 534:
        break
    print(i, end=' ')  # 1 2 3 4 234 456 678

# itertools.repeat(elem, n=Inf) - повторяет elem n раз
iterator_repeat = itertools.repeat(2, 17)
for i in iterator_repeat:
    print(i, end=' ')  # 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2

# itertools.accumulate(iterable) - аккумулирует суммы.
print(list(itertools.accumulate([1, 2, 3, 4, 5, 13, 1444])))  # [1, 3, 6, 10, 15, 28, 1472]

# itertools.chain(*iterables) - возвращает по одному элементу из первого итератора, потом из второго,
# до тех пор, пока итераторы не кончатся.
itertools_chained = itertools.chain('ab', [33, 234, 654])
print(next(itertools_chained))  # a
print(next(itertools_chained))  # b
print(next(itertools_chained))  # 33
print(next(itertools_chained))  # 234
print(next(itertools_chained))  # 654


# есть еще chain.from_iterable
# https://stackoverflow.com/questions/15004772/what-is-the-difference-between-chain-and-chain-from-iterable-in-itertools
def gen_iterables():
    for item in range(10):
        yield range(item)


from_iterable = itertools.chain.from_iterable(gen_iterables())
for i in range(21):
    print(next(from_iterable))

# itertools.combinations(iterable, [r]) - комбинации длиной r из iterable без повторяющихся элементов.
print(list(itertools.combinations('ABCD', 1)))  # [('A',), ('B',), ('C',), ('D',)]
print(
    list(itertools.combinations('ABCD', 2)))  # [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
print(list(itertools.combinations('ABCD', 3)))  # [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]
print(list(itertools.combinations('ABCD', 4)))  # [('A', 'B', 'C', 'D')]

# itertools.compress(data, selectors) - поддерживает либо 1, либо 0. возвращает елемент, если 1, не возвращает если 0
print(list(itertools.compress('ABCDEF', [1, 0, 0, 0, 1, 1])))  # ['A', 'E', 'F']

# itertools.dropwhile(func, iterable) - возвращает элементы iterable, начиная с первого, для которого func вернула ложь
print(list(itertools.dropwhile(lambda x: x < 5, [1, 1, 2, 4, 27, 6, 4, 1])))  # [27, 6, 4, 1]

# itertools.filterfalse(func, iterable) - все элементы, для которых func возвращает ложь
print(list(itertools.filterfalse(lambda x: x < 5, [1, 1, 2, 4, 27, 6, 4, 1])))  # [27, 6]

# itertools.takewhile(func, iterable) - элементы до тех пор, пока func возвращает истину.
print(list(itertools.takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])))  # [1, 4]

# itertools.groupby(iterable, key=None) - группирует элементы по значению. Значение получается применением
# функции key к элементу (если аргумент key не указан, то значением является сам элемент).
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"),
          ("vehicle", "speed boat"), ("vehicle", "school bus")]
for key, group in itertools.groupby(things, lambda x: x[0]):
    # print(str(key), list(group))
    # # animal [('animal', 'bear'), ('animal', 'duck')]
    # # plant [('plant', 'cactus')]
    # # vehicle [('vehicle', 'speed boat'), ('vehicle', 'school bus')]
    for thing in group:
        print("A %s is a %s." % (thing[1], key))
    print()
# A bear is a animal.
# A duck is a animal.
#
# A cactus is a plant.
#
# A speed boat is a vehicle.
# A school bus is a vehicle.


# itertools.islice(iterable[, start], stop[, step]) - итератор, состоящий из среза
print(list(itertools.islice(range(0, 200), 23, 188, 19)))  # [23, 42, 61, 80, 99, 118, 137, 156, 175]

# itertools.permutations(iterable, r=None) - перестановки длиной r из iterable
for i in itertools.permutations(['купить', 'квартиру', 'москва', 'университет'], r=4):
    # у нас 4 сущности, и чтобы получить все комбинации с ними мы пишем r=4
    print(i)
# ('купить', 'квартиру', 'москва', 'университет')
# ('купить', 'квартиру', 'университет', 'москва')
# ('купить', 'москва', 'квартиру', 'университет')
# ('купить', 'москва', 'университет', 'квартиру')
# ('купить', 'университет', 'квартиру', 'москва')
# ('купить', 'университет', 'москва', 'квартиру')
# ('квартиру', 'купить', 'москва', 'университет')
# ('квартиру', 'купить', 'университет', 'москва')
# ('квартиру', 'москва', 'купить', 'университет')
# ('квартиру', 'москва', 'университет', 'купить')
# ('квартиру', 'университет', 'купить', 'москва')
# ('квартиру', 'университет', 'москва', 'купить')
# ('москва', 'купить', 'квартиру', 'университет')
# ('москва', 'купить', 'университет', 'квартиру')
# ('москва', 'квартиру', 'купить', 'университет')
# ('москва', 'квартиру', 'университет', 'купить')
# ('москва', 'университет', 'купить', 'квартиру')
# ('москва', 'университет', 'квартиру', 'купить')
# ('университет', 'купить', 'квартиру', 'москва')
# ('университет', 'купить', 'москва', 'квартиру')
# ('университет', 'квартиру', 'купить', 'москва')
# ('университет', 'квартиру', 'москва', 'купить')
# ('университет', 'москва', 'купить', 'квартиру')
# ('университет', 'москва', 'квартиру', 'купить')


# itertools.product(*iterables, repeat=1) - аналог вложенных циклов
print(list(itertools.product('ABCD', 'xy')))
# [('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y'), ('C', 'x'), ('C', 'y'), ('D', 'x'), ('D', 'y')]


# itertools.starmap(function, iterable) - применяет функцию к каждому элементу
# последовательности (каждый элемент распаковывается)
print(list(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)])))  # [32, 9, 1000]

# itertools.tee(iterable, n=2) - кортеж из n итераторов
iter1, iter2, iter3, iter4 = itertools.tee([1, 2, 3], 4)
print(list(iter1))  # [1, 2, 3]
print(list(iter2))  # [1, 2, 3]
print(list(iter3))  # [1, 2, 3]
print(list(iter4))  # [1, 2, 3]

# itertools.zip_longest(*iterables, fillvalue=None) - как встроенная функция zip, но берет самый
# длинный итератор, а более короткие дополняет fillvalue.
print(list(itertools.zip_longest('ABCD', 'xy', fillvalue='-')))  # [('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')]
