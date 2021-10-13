# |||||||||||||||||||||||||||||||||||||||||||||||||
# # Урок 38 Пользовательские исключения в Python Custom Exception Python

class MyFirstException(Exception):  # always it's better to inheritance from class Exception
    # to avoid excess essence
    """This is my first exception"""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'MyException ({self.message})'
        else:
            return 'MyException is empty'


# raise MyFirstException('Hello', 1, 2, 3)


# Also you can create yous oun hierarchy of exceptions. Fof example for game 'snake'
class SnakeExceptionBase(Exception):
    """Base class of exceptions of game 'snake'"""


class SnakeBorderException(SnakeExceptionBase):
    """Exception of touching the snake with borders"""


class SnakeTailException(SnakeExceptionBase):
    """Touching the snake with her body"""
