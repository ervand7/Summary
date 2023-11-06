def isHappy(n: int) -> bool:
    set_ = set()
    while n != 1:
        n: int = sum([pow(int(i), 2) for i in str(n)])
        if n not in set_:
            set_.add(n)
        else:
            return False
    return True
