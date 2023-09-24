def say():
    print("say's function worked out!")


def decorator(func):
    def inner(*args, **kwargs):
        print('start decorator')
        func(*args, **kwargs)
        print('finish decorator')

    print(hex(id(inner)))  # 0x7ff5b025a820
    return inner


print(hex(id(say)))  # 0x7ff5b01de4c0
say = decorator(say)
print(hex(id(say)))  # 0x7ff5b025a820 <- now it links to inner

say()
# start decorator
# say's function worked out!
# finish decorator
