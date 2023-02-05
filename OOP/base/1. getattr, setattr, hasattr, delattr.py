class Ivan:
    age = 15

    @staticmethod
    def say_hello():
        print('Hello')


print(hasattr(Ivan, 'say_hello'))  # True
getattr(Ivan, 'say_hello', None)()  # Hello

setattr(Ivan, 'say_hello', 55)
print(getattr(Ivan, 'say_hello', None))  # 55

delattr(Ivan, 'say_hello')
print(hasattr(Ivan, 'say_hello'))  # False
