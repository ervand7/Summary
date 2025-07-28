# my solution
def largest_integer(num: int) -> int:
    evens, odds = [], []
    num_str = str(num)
    for i in num_str:
        v = int(i)
        if v % 2 == 0:
            evens.append(v)
        else:
            odds.append(v)

    evens.sort()
    odds.sort()

    result = []
    for i in num_str:
        if int(i) % 2 == 0:
            result.append(str(evens.pop()))
        else:
            result.append(str(odds.pop()))

    return int("".join(result))
