# my solution
def add_digits(num: int) -> int:
    lst = []
    while True:
        item = num % 10
        lst.append(item)
        num = num // 10
        if num == 0:
            s = sum(lst)
            if s < 10:
                return s

            lst = []
            num = s


# ChatGPT solution
def add_digits(num: int) -> int:
    if num == 0:
        return 0
    else:
        return 1 + (num - 1) % 9
