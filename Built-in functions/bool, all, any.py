# фукция bool. Все, что не 0, не '', не [], не () - все, даже отрицательные числа - True. Остальное - False
print(bool([]))
print(bool(0))
print(bool(-0.001))

# фукция all принимает итерабельную последовательность. И если в этой последовательности есть
# хотя бы 1 пустой элемент, возвращает False. Когда нет пустых эелементов - True
a = [1, 2, '3', ()]  # False
# print(all(a))

# фукция any также принимает итерабельную последовательность. И, в случае если хотя бы 1 элемент
# не пустой, она возвращает True. Если все элементы пустые, то False
b = (1, 0, 0, [])  # True
# print(any(b))
