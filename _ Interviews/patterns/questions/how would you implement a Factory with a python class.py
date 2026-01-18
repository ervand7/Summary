# I implement factories in Python using a registry that maps keys to classes
# and a classmethod that instantiates them.

class Factory:
    _registry = {}

    @classmethod
    def register(cls, key, impl):
        cls._registry[key] = impl

    @classmethod
    def create(cls, key, *args, **kwargs):
        return cls._registry[key](*args, **kwargs)


class A:
    def run(self):
        print("A running")


class B:
    def run(self):
        print("B running")


Factory.register("a", A)
Factory.register("b", B)

obj = Factory.create("a")
obj.run()
