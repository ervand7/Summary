from typing import List, Dict, Optional, Any, Union


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

# ______________________________________________________
e: Any = 12  # в "e" может содержаться любой тип


# ______________________________________________________
def add_numbers(value1: int, value2: Optional[int]):  # Optional означает, что "value2"
    # у нас может быть либо int, либо None
    return value1 + value2


# ______________________________________________________
def some(value1: int, value2: Union[int, float, str]):  # Union означает, что "value2"
    # у нас может попадать одно из перечисленных значений
    return value1 + value2
