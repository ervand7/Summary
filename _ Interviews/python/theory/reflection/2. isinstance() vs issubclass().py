class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True
print(isinstance(Dog, Animal))  # False

print(issubclass(Dog, Animal))  # True
print(issubclass(Animal, Dog))  # False
