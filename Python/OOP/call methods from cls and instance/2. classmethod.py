class Ivan:
    age = 15

    @classmethod
    def say_hello(cls):
        print(cls.__dict__)
        print('hello')


# 1) можно вызвать напрямую от класса
Ivan.say_hello()  # hello
# {'__module__': '__main__', 'age': 15, 'say_hello': <classmethod object at 0x7fb788279a30>, '__dict__': <attribute '__dict__' of 'Ivan' objects>, '__weakref__': <attribute '__weakref__' of 'Ivan' objects>, '__doc__': None}


# 2) можно вызвать напрямую от класса, создав временный экземпляр
Ivan().say_hello()  # hello
# {'__module__': '__main__', 'age': 15, 'say_hello': <classmethod object at 0x7faf68171a30>, '__dict__': <attribute '__dict__' of 'Ivan' objects>, '__weakref__': <attribute '__weakref__' of 'Ivan' objects>, '__doc__': None}


# 3) можно вызвать от экземпляра
ivan = Ivan()
ivan.say_hello()  # hello
# {'__module__': '__main__', 'age': 15, 'say_hello': <classmethod object at 0x7faf68171a30>, '__dict__': <attribute '__dict__' of 'Ivan' objects>, '__weakref__': <attribute '__weakref__' of 'Ivan' objects>, '__doc__': None}


# нужно понимать, что во всех случаях мы имеем доступ уже к самому классу (cls)
# и его возможностям, а не к экземпляру (self)
