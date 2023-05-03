# Функция, которая противоположна функции zip. Она разъединяет элементы в отдельные коллекции
a = [1, 2, 3, 4]
b = 'qwer'
c = ('qw', 'er', 'ty', 'ui')
rez = list(zip(a, b, c))
print(rez)

col1, col2, col3 = zip(*rez)
print(col1, col2, col3)
