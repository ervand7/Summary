# Урок 36 Обработка исключений
# Под <try> мы можем писать сколько угодно разных except
try:
    int('hello')
    print(123)  # won't work
    1 / 0  # won't work
    a + b  # won't work
except ValueError:
    print('error ValueError')
except ZeroDivisionError:
    print('error ZeroDivisionError')
except NameError:
    print('error NameError')


# Указать универсальное-глобальное исключение
try:
    'qwe' / 123.321
except:  # similarly BaseException. If we specify only one statement 'except' here get all exceptions from class Except
    print('All excepts')
# но лучше таких вещей не делать и указать хотя бы Exception
try:
    'asd' / 123.321
except Exception:
    print('All excepts')


# try - except - else (указыватся только 1 раз) - finally (указыватся только 1 раз)
try:
    1 / 0
except (KeyError, IndexError):  # мы можем за раз картежем прописать несколько исключений
    print('LookupError')  # parent's class
except ZeroDivisionError:
    print('ZeroDivisionError')
else:  # исполняется в случае, если код правильный и не понадобилось обрабатывать исключение
    print('Good')
finally:  # исполняется вконце в любом случае, не зависимо ни от чего
    print('end')


# Псевдонимы
try:
    3 / 0
except ZeroDivisionError as z:
    print(f"{z.__repr__.__call__()}")
