# Попробуем поработать без импортированного модуля
a = [1, 2, 3]
b = a.copy()
b.insert(2, [5, 6])
print(b)  # [1, 2, [5, 6], 3]
print(a)  # [1, 2, 3]

# ___________________________________________________________________________________________
# Поработаем с импортированным модулем
from copy import copy, deepcopy

# copy предназначена для копирования объектов, которые НЕ содержат вложенные элементы
a = [1, 2, 3, [1, 2, 3]]
b = copy(a)

b[3].append(4)
print(b)  # [1, 2, 3, [1, 2, 3, 4]]
# видим, что здесь copy не справляется
print(a)  # [1, 2, 3, [1, 2, 3, 4]]

# deepcopy предназначена для копирования объектов, которые содержат вложенные элементы
a = [1, 2, 3, [1, 2, 3]]
b = deepcopy(a)
b[3].append(4)
print(b)  # [1, 2, 3, [1, 2, 3, 4]]
print(a)  # [1, 2, 3, [1, 2, 3]]
