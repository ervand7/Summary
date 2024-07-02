# You should understand that err is just instance of error class

try:
    1/0
except ZeroDivisionError as err:
    print(isinstance(err, ZeroDivisionError))
    print(err.__dict__)  # {}
    print(err.__doc__)  # Second argument to a division or modulo operation was zero.
    print(err.__sizeof__())  # 64
    print(err)  # division by zero
    print(err.__str__())  # division by zero

