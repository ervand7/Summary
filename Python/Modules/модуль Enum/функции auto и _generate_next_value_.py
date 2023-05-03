# документация: https://docs.python.org/3/library/enum.html#using-automatic-values
from enum import Enum, auto


class Color(Enum):
    RED = auto()
    BLUE = auto()
    GREEN = auto()


print(list(Color))  # [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]


# _______________________________________________________________________
class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class Ordinal(AutoName):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


print(list(Ordinal))  # [<Ordinal.NORTH: 'NORTH'>, <Ordinal.SOUTH: 'SOUTH'>, <Ordinal.EAST: 'EAST'>, <Ordinal.WEST: 'WEST'>]
