class Ivan:
    def say_hello(self) -> str:
        return "Hello"


Vasya = Ivan
# the same addr
print(hex(id(Ivan)))  # 0x7fcdc9f2da30
print(hex(id(Vasya)))  # 0x7fcdc9f2da30
print(Vasya == Ivan)  # True

# Ivan will receive `qwerty` field
Vasya.qwerty = 333
print(Ivan.qwerty)  # 333


# let's patch Ivan say_hello function
def say_another_hello(self: Ivan) -> str:
    return "Another hello"


# the same addresses
print(hex(id(Ivan.say_hello)))  # 0x7f79880c9430
print(hex(id(Vasya.say_hello)))  # 0x7f79880c9430

# addr changed
Vasya.say_hello = say_another_hello
print(hex(id(Ivan.say_hello)))  # 0x7fbf380c9820
print(hex(id(Vasya.say_hello)))  # 0x7fbf380c9820

ivan = Ivan()
ivan2 = Ivan()
print(ivan.say_hello())  # Another hello
print(ivan2.say_hello())  # Another hello

# addr changed
Vasya.say_hello = 4
print(hex(id(Ivan.say_hello)))  # 0x7fc45002e990
print(hex(id(Vasya.say_hello)))  # 0x7fc45002e990
print(hex(id(ivan.say_hello)))  # 0x7fc45002e990
print(hex(id(ivan2.say_hello)))  # 0x7fc45002e990
print(Ivan.say_hello)  # 4
print(ivan.say_hello)  # 4
