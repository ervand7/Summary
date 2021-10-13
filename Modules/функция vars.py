class Foo:
    def __init__(self, a=5, b=10):
        self.a = a
        self.b = b


print(vars(Foo()))
print(vars(Foo))

example = Foo(12, 34)
print(vars(example))  # {'a': 12, 'b': 34}
