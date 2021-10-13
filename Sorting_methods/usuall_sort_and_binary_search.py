# ||||||||||||||||| Сравним скорость работы линейного и бинарного поиска |||||||||||||||||
import datetime
from random import randint


def linear_search(array, number):
    """The complexity of this algorithm is O(n) - linear search"""
    sorted_array = sorted(array)
    for i in range(len(sorted_array)):
        if sorted_array[i] == number:  # если значение, которое находится по индексу [i] в array равно number
            return f'{i} - linear search'
    return 'Искомого числа нет в array (linear search).'  # зададим дефолтное значение


def binary_search(array, number):
    """The complexity of this algorithm is O(n * log (n) - binary search"""
    sorted_array = sorted(array)
    lower_bound = 0  # нижняя граница списка
    upper_bound = len(sorted_array)  # верхняя граница

    while lower_bound <= upper_bound:
        center = (lower_bound + upper_bound) // 2  # в данном случае //, а не / потому, что индекс не может быть float

        if sorted_array[center] == number:  # если центр. элемент списка равен искомому number, то сразу его выводим
            return f'{center} - binary search'
        elif sorted_array[center] > number:  # Скажем, что у нас в списке 10 эл., и мы ищем элемент (number), значение
            # которого равно 3. В данном случае array[center] является array[с индексом, значение которого равно 5].
            # И поскольку 5 > 3, то мы верхнюю границу (upper_bound), которая до этого была равна 10 спускаем до 4.
            # И уже ище не в диапазоне от 0 до 10, а в диапазоне от 0 до 5, что в 2 раза сокращает наш поиск.
            upper_bound = center - 1  # - 1 здесь для экономии энергии, так как центральное число мы уже проверяли
        elif sorted_array[center] < number:  # инверсируем вышенаписанный способ
            lower_bound = center + 1  # + 1 здесь для экономии энергии, так как центральное число мы уже проверяли

    return 'Искомого числа нет в array (binary search).'  # поскольку для генерации чисел мы используем модуль
    # from random import randint, то искомого числа (number) попросту может не оказаться в array. И мы выводим
    # дефолтное предупреждение


if __name__ == '__main__':
    my_array = list(range(80000000))

    linear_start = datetime.datetime.now()
    print(linear_search(my_array, 13341432))
    print(f'End linear: {datetime.datetime.now() - linear_start}')

    binary_start = datetime.datetime.now()
    print(binary_search(my_array, 13341432))
    print(f'End binary: {datetime.datetime.now() - binary_start}\n')
