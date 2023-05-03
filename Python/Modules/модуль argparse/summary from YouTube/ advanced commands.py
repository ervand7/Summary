# source: https://www.youtube.com/watch?v=792UnrSxD6w
# этот файл (скрипт) запускается в терминале командой:
# $python3 '/Users/USER/Desktop/My_best_summary_about_python/summary/боевые проблемы/модуль_argparse/summary from YouTube/ advanced commands.py' и далее прописываем аргументы
import argparse
"""
action='store'                   - default parameter of argparse module

action='store_const', const='10' - set parameter constant value

action='store_true'              - True in Namespace(my_parameter=) if the parameter was passed

action='store_false'             - False in Namespace(my_parameter=) if the parameter was passed

nargs=2                          - amount of arguments which we can pass to parameter (exact to parameter, not to script)

choices=[1, 2, 3]                - choice is restricted by following values

dest='B'                         - rename parameter
"""

parser = argparse.ArgumentParser()

parser.add_argument('-m', '--my_parameter', dest='B')

args = parser.parse_args()

print(args)
