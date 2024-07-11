# the second condition (some()) even will not be checked

a, b = 1, 0


def some():
    global b
    b = 1
    print("Hello")
    return True


if a == 1 or some():
    print("World")

print(b)  # 0
