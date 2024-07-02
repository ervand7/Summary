class Ivan:
    age = 15

    def say_hello(self):
        print(f'hello {self.age}')


# 1) можно вызвать напрямую от класса, передав временный экземпляр
Ivan.say_hello(Ivan())  # hello 15

# 2) можно вызвать напрямую от класса, создав временный экземпляр
Ivan().say_hello()  # hello 15

# 3) можно вызвать от экземпляра
ivan = Ivan()
ivan.say_hello()  # hello 15

# нужно понимать, что во всех случаях мы имеем доступ к self и его возможностям
