# 3.8:
from typing import Dict


def pint_phone_book(book: Dict[str, str]) -> None:
    for name, phone in book.items():
        print(f'{name.ljust(12)} - {phone}')


pint_phone_book(
    {
        'hello': '01',
        'hi': '02',
        'world': '03',
    }
)
# hello        - 01
# hi           - 02
# world        - 03


# 3.9:
# не нужно импортировать Dict из typing. Используем встроенный dict
def pint_phone_book2(book: dict[str, str]) -> None:
    for name, phone in book.items():
        print(f'{name.ljust(12)} - {phone}')


pint_phone_book2(
    {
        'hello': '01',
        'hi': '02',
        'world': '03',
    }
)
# hello        - 01
# hi           - 02
# world        - 03
