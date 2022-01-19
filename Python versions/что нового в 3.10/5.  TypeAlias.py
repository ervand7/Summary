from typing import TypeAlias

# 3.9
FileName = str


def parse(file: FileName) -> None: ...


# 3.10
FileName: TypeAlias = str


def parse2(file: FileName) -> None: ...
