from typing import overload, Union, Literal
"""
Этот декоратор нужен лишь чтобы подробно описать функцию, которая
в качестве входящих параметров принимает разные параметры.
И описание каждого параметра мы прописываем отдельно.
"""


@overload
def my_func(arg: Literal[True] = True) -> str: ...


@overload
def my_func(arg: Literal[False]) -> int: ...


def my_func(arg: bool = True) -> Union[int, str]:
    if arg:
        return "something"
    else:
        return 0
