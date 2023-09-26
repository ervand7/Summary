# На самом деле мы можем хакнуть и присвоить экземпляру класса
# метод, которого нет у самого класса
class Ivan:
    name = "Ivan"

    def say_hello(self):
        print(f"Hello, {self.name}")


def say_hello(self):
    print(hex(id(say_hello)))  # 0x7f9e300cef70
    print(f"Hello, {self.name}")


i = Ivan()
print(i.__dict__)  # {}

setattr(i, "say_hello", say_hello)
getattr(i, "say_hello")(i)  # Hello, Ivan
print(i.__dict__)  # {'say_hello': <function say_hello at 0x7f9e300cef70>}
