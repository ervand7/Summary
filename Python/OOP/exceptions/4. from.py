# use `from` to improve traceback

class MyException(Exception):
    """ My exception """


try:
    {"hello": "world"}[777]
except KeyError as err:
    raise MyException from err

# Traceback (most recent call last):
#   File "/Users/ervand_agadzhanyan/Desktop/Summary/Python/OOP/exceptions/4. from.py", line 7, in <module>
#     {"hello": "world"}[777]
# KeyError: 777
#
# The above exception was the direct cause of the following exception:
#
# Traceback (most recent call last):
#   File "/Users/ervand_agadzhanyan/Desktop/Summary/Python/OOP/exceptions/4. from.py", line 9, in <module>
#     raise MyException from err
# __main__.MyException