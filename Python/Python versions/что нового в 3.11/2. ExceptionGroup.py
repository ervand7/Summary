try:
    raise ExceptionGroup("описание группы исключений", [
        ValueError("111"),
        TypeError("222"),
        IndexError("333"),
        ValueError("444")
    ])
except* ValueError as eg:
    for exc in eg.exceptions:
        print(exc)
except* TypeError as eg:
    for exc in eg.exceptions:
        print(exc)
except* IndexError as eg:
    for exc in eg.exceptions:
        print(exc)

# or so
except* Exception as eg:
    for exc in eg.exceptions:
        print(exc)

# 111
# 444
# 222
# 333
