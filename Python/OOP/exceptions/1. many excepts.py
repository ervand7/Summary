# Под try мы можем писать сколько угодно разных except
try:
    int('hello')
    print(123)  # won't work
    1 / 0  # won't work
    a + b  # won't work
except ValueError as e:
    print(e)  # invalid literal for int() with base 10: 'hello'
except ZeroDivisionError as e:
    print(e)
except NameError as e:
    print(e)
