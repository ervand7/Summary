class Ivan:
    name = "Ivan"

    @classmethod
    def change_name(cls, arg):
        cls.name = arg


a = Ivan()
b = Ivan()

a.change_name("Vasya")
print(a.name)  # Vasya
print(b.name)  # Vasya
