# val changes because we create a new var inside func

n = 1
print(hex(id(n)))  # 0x7fbb3002e930


def some():
    global n
    print(hex(id(n)))  # 0x7fbb3002e930
    n = 333
    print(hex(id(n)))  # 0x7fc7680884f0  <- addr changed after changing global val


some()
print(n)  # 333
