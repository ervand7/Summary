import traceback
from typing import List


class DefendedVector(object):
    def __init__(self, vector: List[int]):
        self.__v = vector

    def __enter__(self):
        """
        Вызывается при запуске менеджера контекста.
        Когда мы будем писать: with DefendedVector(item) as dv:
        то в dv попадет то, что возвращает __enter__
        """
        self.__temp = self.__v[:]
        print(hex(id(self.__temp)))  # 0x7fd0f81a5cc0
        return self.__temp

    def __exit__(
            self,
            exc_type: type,
            exc_val: Exception,
            exc_tb: traceback
    ):
        """
        Вызывается в момент перед выходом из менеджера контекста, либо
        при возникновении ошибки.
        exc_type : Тип зафиксированного исключения, либо None.
        exc_val : Объект зафиксированного исключения, либо None.
        exc_tb : Трассировка стека для зафиксированного исключения, либо None.
        """
        print(exc_type)  # <class 'IndexError'>
        print(exc_val)  # list index out of range
        print(exc_tb)  # <traceback object at 0x7feb481c2f00>

        print(hex(id(self.__v)))  # 0x7fc0d8166640
        if exc_type is None:
            self.__v[:] = self.__temp

        # Если прописать True, то ошибка будет подавлена и не будет прокинута наружу вне менеджера
        return False


v1 = [1, 2, 3]
v2 = [2, 3]

# С менеджером контекста список v1 останется без изменений
try:
    print(hex(id(v1)))  # 0x7fc0d8166640
    with DefendedVector(v1) as dv:
        print(hex(id(dv)))  # 0x7fd0f81a5cc0

        for i, _ in enumerate(dv):
            dv[i] += v2[i]
except:
    print(v1)  # [1, 2, 3]

# Без менеджера контекста v1 изменился
try:
    for i, _ in enumerate(v1):
        v1[i] += v2[i]
except:
    print(v1)  # [3, 5, 3]
