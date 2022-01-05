# source: https://www.youtube.com/watch?v=792UnrSxD6w
# этот файл (скрипт) запускается в терминале командой:
# $python3 '/Users/USER/Desktop/My_best_summary_about_python/summary/боевые проблемы/модуль_argparse/summary from YouTube/ base commands.py' и далее прописываем аргументы
import argparse

"""
The values of the arguments:
default -- The value to be produced if the option is not specified.

required -- True if the action must always be specified at the
            command line. This is only meaningful for optional command-line
            arguments.
"""

# после импорта argparse мы должны создать парсер
parser = argparse.ArgumentParser()
# добавление аргументов
# 1) Позиционные аргументы
parser.add_argument("a", type=int, help='First argument')
parser.add_argument("b", type=int, help='Second argument')
# 2) Optional, именнованные. Где '-m' - это скращенный вариант от '--my_parameter'. Указываем и то, и то
parser.add_argument('-m', '--my_parameter', action='store', help='What to do with this numbers?')
args = parser.parse_args()
print(args)


def summa(a, b):
    print(a + b)


def minus(a, b):
    print(a - b)


if args.action == 'summa':
    summa(args.a, args.b)
elif args.action == 'minus':
    minus(args.a, args.b)
else:
    print('OOPs')
