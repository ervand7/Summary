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
Что также нужно прочесть:
 ● Лучшая статья по всем типам данных: 
https://pythonworld.ru/tipy-dannyx-v-python
 
 ● Массив в python
https://codecamp.ru/blog/python-arrays/
https://pythonworld.ru/moduli/modul-array-massivy-v-python.html
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
