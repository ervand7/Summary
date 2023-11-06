def rec(x):
    if x < 4:
        print(x, end=' ')
        rec(x + 1)


rec(1)  # 1 2 3
