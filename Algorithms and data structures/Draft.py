def is_happy(n: int) -> bool:
    count = 0
    while True:
        if count == 100:
            return False
        data = [int(i) for i in list(str(n))]
        p = sum([i ** 2 for i in data])
        if p == 1:
            return True
        n = p

        count+=1


print(is_happy(2))