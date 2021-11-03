"""
|||||||||| Вопросы на собеседовании ||||||||||
Актуальные версии Python
● Python 3.x vs Python 2.7
● Основные отличия
_______________________________________________

Сильные стороны Python:
● кроссплатформенность
● мультипарадигмальность (ООП, функциональное и императивно-процедурное программирование)
● динамическая типизация
● поддержка юникода из коробки (что такое юникод: https://www.youtube.com/watch?v=4MFcmreAUhs )
● жесткие требования к написанию кода (PEP 8)

_____________________________________________
Слабые стороны Python:
● производительность
● многопоточность (GIL (global interpreter lock) - глобальная блокировка интерпретатора https://www.youtube.com/watch?v=AWX4JnAnjBE )
● реализация функциональной парадигмы
● динамическая типизация

_____________________________________________
Области применения
● веб-разработка (django, flask, tornado, twisted)
● автоматизация процессов - DevOps (ansible, fabric, salt stack)
● автоматизация тестирования (behave!, robot framework, pytest, nose, unittest)
● наука и анализ данных (scipy, numpy, pandas)

● desktop applications (pyqt, pygtk)
● gamedev
● IoT (Micro Python)
● mobile applications (Kivy)
"""

# Подробнее о динамической типизации: https://www.youtube.com/watch?v=cbOq9HNU8Yg
x = 's'
print(hex(id(x)))  # 0x7f995adb1730
x = 3
print(hex(id(x)))  # 0x10e348b00

"""
Вопросы, которые нужно погуглить:
 ● отличие компиляцора от интерпретатора
 ● что такое абстракция
 ● Двоичное дерево https://www.youtube.com/watch?v=9o_i0zzxk1s&list=LL&index=13&t=1s
 ● Односвязный список https://www.youtube.com/watch?v=C9FK1pHLnhI&list=LL&index=12&t=655s
 ● Двусвязный список https://www.youtube.com/watch?v=lQ-lPjbb9Ew&t=434s
 ● Лучшая статья по всем типам данных: https://pythonworld.ru/tipy-dannyx-v-python
 
 ● Массив в python
https://codecamp.ru/blog/python-arrays/
https://pythonworld.ru/moduli/modul-array-massivy-v-python.html
"""



"""
Концепция Big O
main article https://stackabuse.com/big-o-notation-and-algorithm-analysis-with-python-examples/
main video https://www.youtube.com/watch?v=ZRdOb4yR0kk
other important video:
https://www.youtube.com/watch?v=kwmQwGbAh28
https://www.youtube.com/watch?v=eJRg4qr7qAo&list=LL&index=2
https://www.youtube.com/watch?v=mgvbBU4bMF8&list=LL&index=3&t=168s
https://www.youtube.com/watch?v=72jqTtfw2z4&list=LL&index=1
 ● O(1)
когда у нас гарантированно одно действие: например, найти индекс у сортированного элемента

 ● O(n)
когда сложность растет в линейном порядке параллельно с увеличением входных параметров
или когда мы имеем 2 подряд идущих невложенных зависимых цикла: O(n + n) = O(n)

 ● O(n^2)
при вложенных циклах, а так же при ситуациях где изначально при запуски и внешнего, и вложенного
циклов длины n внешней и n внутренней равны, а затем одна из них сокращается,
скажем, в 2 раза: O(n^2 / 2) ≈ O(n^2)

 ● O(n + other)
когда идут 2 подряд независимых друг от друга цикла

 ● O(n * other)
когда внешний цикл длиной n, а внутренний цикл длинной other

 ● O(log n)
при использовании бинарного поиска по сортированному контейнеру (ищем по принципу двоичного дерева)

 ● O(n * log(n))
при использ. бинарного поиска по несортированному контейнеру (ищем по принципу двоичного дерева)

 ● Big O показывает темп роста функции. Следовательно мы не учитываем константы и неважную сложность
 ● Последовательность действий - сложение. Вложенные действия - умножение
 ● Для алгоритма, где на каждой итерации берется половина элементов сложность 
будет включать O(log n) или O(n * log(n))
"""


# a problem from lesson
from typing import Optional, List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums):
                if index1 + index2 == target:  # нельзя, чтобы сумма одного и того же числа давала результат
                    continue
                if num1 + num2 == target:
                    return [index1, index2]


# some simplified variant
a = Solution()
my_nums = [4, 2, 3, 5, 1, 0, 9]
my_target = 9
print(a.two_sum(my_nums, my_target))


class BestSolution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for indx, number in enumerate(nums):
            dct[target - number] = indx
            if number in dct:
                return [dct[number], indx]


b = BestSolution()
my_nums3 = [4, 2, 3, 5, 1, 0, 9]
my_target3 = 9
print(b.two_sum(my_nums3, my_target3))

# _______________________________________________________________________
# другое:
# # we can visualize with this library
# import matplotlib.pyplot
#
# x = [2, 4, 6, 8, 10, 12]
#
# y = [2, 4, 6, 8, 10, 12]
#
# matplotlib.pyplot.plot(x, y, 'b')
# matplotlib.pyplot.xlabel('my_x')
# matplotlib.pyplot.ylabel('my_y')
# matplotlib.pyplot.title('It is my table :-)')
#
# # matplotlib.pyplot.show()
