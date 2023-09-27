class Point:
    def __new__(cls, *args, **kwargs) -> "Point":
        """
        __new__ в отличие от __init__ вызывается до создания объекта.
        Если при реализации __new__ не прописать вызов __new__ от
        базового класса, то у нас даже __init__ не отработает и
        экземпляр класса не создастся.
        *args, **kwargs нужно обязательно прописывать, так как
        при создании экземпляра класса p = Point(1, 2), 1 и 2 будут
        пропускаться как раз через *args, **kwargs.
        """
        # We see that Point and cls are the same thing
        print(hex(id(Point)))  # 0x7faa84127490
        print(hex(id(cls)))  # 0x7faa84127490
        print(args)  # (1,)
        print(kwargs)  # {'y': 2}

        new_instance = super().__new__(cls)
        # here is addr of new instance (self)
        print(hex(id(new_instance)))  # 0x7faa680abf10
        return new_instance

    def __init__(self, x=0, y=0):
        """Параметр self ссылается на экземпляр класса."""
        print(hex(id(self)))  # 0x7faa680abf10
        self.x = x
        self.y = y


p = Point(1, y=2)
