def rec(val):
    print(val)
    if val < 4:
        rec(val + 1)
    print(val)


rec(1)

# 1
# 2
# 3
# 4
# 4
# 3
# 2
# 1
