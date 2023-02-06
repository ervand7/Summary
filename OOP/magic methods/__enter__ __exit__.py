import traceback
from typing import List, Type


class DefendedVector(object):
    def __init__(self, vector: List[int]):
        self.__v = vector

    def __enter__(self):
        """
        Вызывается при запуске менеджера контекста.
        Когда мы будем писать:
        with DefendedVector(item) as dv:
        то в dv попадет то, что возвращает __enter__
        """
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(
            self,
            exc_type: Type[Exception],
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
        if exc_type is None:
            self.__v[:] = self.__temp

        return False  # Если прописать True, то ошибка будет подавлена и не будет прокинута наружу за менеджер


v1 = [1, 2, 3]
v2 = [2, 3]

# С менеджером контекста список v1 останется без изменений
try:
    with DefendedVector(v1) as dv:
        for i, _ in enumerate(dv):
            dv[1] += v2[i]
except:
    print(v1)  # [1, 2, 3]

# Без менеджера контекста v1 изменился
try:
    for i, _ in enumerate(v1):
        v1[i] += v2[i]
except:
    print(v1)  # [3, 5, 3]
