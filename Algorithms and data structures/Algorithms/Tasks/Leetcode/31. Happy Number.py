# mu solution
def is_happy(self, n: int) -> bool:
    count = 0
    while True:
        if count == 7:  # это число получено опытным путем
            return False
        p = sum([int(i) ** 2 for i in str(n)])
        if p == 1:
            return True
        n = p

        count += 1


def is_happy2(n: int) -> bool:
    unique = set()
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n not in unique:
            unique.add(n)
        else:
            return False
    return True
