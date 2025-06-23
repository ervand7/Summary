# after using setter, we can see property in instance.__dict__

class Ivan:
    __name = "Ivan"

    @property
    def name(self):
        print("getter called")
        return self.__name

    @name.setter
    def name(self, val):
        print("getter called")
        self.__name = val


i = Ivan()
i.name = 4
print(i.__dict__)  # {'_Ivan__name': 4}
print(Ivan.__dict__)  # {'__module__': '__main__', '_Ivan__name': 'Ivan', 'name': <property object at 0x7f7b48138810>, '__dict__': <attribute '__dict__' of 'Ivan' objects>, '__weakref__': <attribute '__weakref__' of 'Ivan' objects>, '__doc__': None}
