# 1) super() возвращает объект-посредник (то есть это не class и не instance),
# через который мы можем вызвать метод родительского класса.
# 2) используется в тех методах, которые переопределяют родительские
# методы и при этом хотят не просто перезатереть их, а расширить их.
# 3) super() всегда стоит вызывать в самом начале переопределяемой функции, чтобы
# логика родительского класса не перезатирала новую логику

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        print(f"Person init for {self}")

    def __str__(self):
        return f"{self.name}, {self.age}"


class Child1(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.surname = "hello"
        print(f"Child1 init for {self}")


class Child2(Person):
    pass


a = Child1("Ivan", 13)
# Person init for Ivan, 13
# Child1 init for Ivan, 13

b = Child2("Ivan", 13)
# Person init for Ivan, 13
