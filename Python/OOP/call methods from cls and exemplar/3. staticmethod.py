class Ivan:
    age = 15

    @staticmethod
    def say_hello():
        print(Ivan.__dict__)
        print('hello')


# 1) можно вызвать напрямую от класса
Ivan.say_hello()
# {'__module__': '__main__', 'age': 15, 'say_hello': <staticmethod object at 0x7fe438079a30>, '__dict__': <attribute '__dict__' of 'Ivan' objects>, '__weakref__': <attribute '__weakref__' of 'Ivan' objects>, '__doc__': None}
# hello

# 2) можно вызвать напрямую от класса, создав временный объект (экземпляр)
Ivan().say_hello()
# {'__module__': '__main__', 'age': 15, 'say_hello': <staticmethod object at 0x7fe438079a30>, '__dict__': <attribute '__dict__' of 'Ivan' objects>, '__weakref__': <attribute '__weakref__' of 'Ivan' objects>, '__doc__': None}
# hello

# 3) можно вызвать от экземпляра
ivan = Ivan()
ivan.say_hello()
# {'__module__': '__main__', 'age': 15, 'say_hello': <staticmethod object at 0x7fe438079a30>, '__dict__': <attribute '__dict__' of 'Ivan' objects>, '__weakref__': <attribute '__weakref__' of 'Ivan' objects>, '__doc__': None}
# hello

# нужно понимать, что во всех случаях мы можем иметь доступ только к классу (Ivan)
# и то, только если внутри статического метода явно дадим на него ссылку

