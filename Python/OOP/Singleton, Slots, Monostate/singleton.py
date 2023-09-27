# creating Singleton. This class can create only one exemplar
class Singleton:
    __instance: "Singleton" = None
    __created = False

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Singleton, cls).__new__(cls)
        else:
            print('Экземпляр класса Singleton уже создан')
        return cls.__instance

    def __init__(self, x, y):
        print("__init__ called")
        # Prevent of passing diff args each time
        if Singleton.__created is False:
            self.x = x
            self.y = y
            Singleton.__created = True


s1 = Singleton(1, 2)  # __init__ called
s2 = Singleton(2, 3)  # __init__ called Экземпляр класса Singleton уже создан
s3 = Singleton(3, 4)  # __init__ called Экземпляр класса Singleton уже создан
s4 = Singleton(4, 5)  # __init__ called Экземпляр класса Singleton уже создан

print(hex(id(s1)))  # 0x7fcbf025de80
print(hex(id(s2)))  # 0x7fcbf025de80
print(hex(id(s3)))  # 0x7fcbf025de80
print(hex(id(s4)))  # 0x7fcbf025de80

print(s1.x, s1.y)  # 1 2
print(s2.x, s2.y)  # 1 2
print(s3.x, s3.y)  # 1 2
print(s4.x, s4.y)  # 1 2
