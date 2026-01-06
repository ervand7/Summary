class Animal:
    def speak(self) -> str:
        pass


class Dog(Animal):
    def speak(self) -> str:
        return "woof"


class Cat(Animal):
    def speak(self) -> str:
        return "meow"


class AnimalFactory:
    def create(self, kind: str) -> Animal:
        if kind == "dog":
            return Dog()
        return Cat()


# Client
factory = AnimalFactory()
animal = factory.create("dog")
print(animal.speak())
