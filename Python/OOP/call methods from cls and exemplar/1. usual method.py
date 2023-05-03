class Ivan:
    age = 15

    def say_hello(self):
        print(self.__dict__)
        print('hello')


# 1) можно вызвать напрямую от класса, создав временный объект (экземпляр)
Ivan().say_hello()
# {}
# hello

# 2) можно вызвать от экземпляра
ivan = Ivan()
ivan.say_hello()
# {}
# hello

# нужно понимать, что в обоих случаях мы имеем доступ к self и его возможностям
