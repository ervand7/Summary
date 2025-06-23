# методы класса также являются аттрибутами
class Ivan:
    name = "Ivan"

    def say_hello(self):
        print(f"Hello, {self.name}")


getattr(Ivan(), "say_hello")()  # Hello, Ivan
