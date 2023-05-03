def say():
    print("say's function worked out!")


def decorator(func):
    def inner(*args, **kwargs):
        print('start decorator')
        func(*args, **kwargs)
        print('finish decorator')

    return inner


say = decorator(say)
say()

# start decorator
# say's function worked out!
# finish decorator
