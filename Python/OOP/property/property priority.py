# Even if instance has local attr with the same name which class property,
# we will work only with property, because it has more priority

class Ivan:
    __name: str = None

    @property
    def name(self) -> str:
        print("getter called")
        return self.__name

    @name.setter
    def name(self, val: str) -> None:
        print("setter called")
        self.__name = val

    @name.deleter
    def name(self) -> None:
        print("deleter called")
        del self.__name


i = Ivan()
i.__dict__["name"] = "Hello"
print(i.__dict__)  # {'name': 'Hello'}

print(i.name)
# getter called
# None

i.name = "Ivan"
# setter called

print(i.name)
# getter called
# Ivan


print(i.__dict__)  # {'name': 'Hello', '_Ivan__name': 'Ivan'}

del i.name
# deleter called
print(i.__dict__)
# {'name': 'Hello'}
