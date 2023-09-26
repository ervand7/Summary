from typing import List, Dict, Optional, Any, Union, Final, Callable


def render_int(num: int) -> str:
    return str(num)


print(render_int.__annotations__)  # {'num': <class 'int'>, 'return': <class 'str'>}


# ______________________________________________________
# проаннотируем таким образом, чтобы в lst могли быть только строки
def list_upper(lst: List[str]):
    for elem in lst:
        print(elem.upper())  # благодаря аннотации, прописанной при объявлении входящих
        # аргументов, PyCharm будет выдавать подсказки после elem.


# ______________________________________________________
a: Dict[str, int] = {'qwe': 123, 'asd': 234}
# такую аннотацию мы получили благодаря тому, что выделили "a" и нажали на желтую лампочку

# Any
e: Any = 12  # в "e" может содержаться любой тип


# Optional
def add_numbers(value1: int, value2: Optional[int]):  # Optional означает, что "value2"
    # у нас может быть либо int, либо None
    return value1 + value2


# Union
def some(value1: int, value2: Union[int, float, str]):  # Union означает, что "value2"
    # у нас может попадать одно из перечисленных значений
    return value1 + value2


# Final - эмуляция константы
Ivan: Final = "Ivan"
Ivan = "Vasya"  # 'Ivan' is 'Final' and could not be reassigned


# Callable
def func(x: int, y: str) -> bool:
    return all([x, y])


def func2(f: Callable[[int, str], bool]) -> None:
    f(1, "hello")


func2(func)
