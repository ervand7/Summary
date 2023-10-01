from typing import Self


class Ivan:
    def __new__(cls, *args, **kwargs) -> Self:
        return super().__new__()
