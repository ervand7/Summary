class Factory:
    _registry = {}

    @classmethod
    def register(cls, key, impl):
        cls._registry[key] = impl

    @classmethod
    def create(cls, key, *args, **kwargs):
        return cls._registry[key](*args, **kwargs)


class A:
    def __init__(self, x):
        self.x = x

    def run(self):
        print(f"A running with x={self.x}")


class B:
    def __init__(self, name, verbose=False):
        self.name = name
        self.verbose = verbose

    def run(self):
        if self.verbose:
            print(f"B running in verbose mode, name={self.name}")
        else:
            print(f"B running, name={self.name}")


Factory.register("a", A)
Factory.register("b", B)

a = Factory.create("a", 10)
a.run()

b = Factory.create("b", "service", verbose=True)
b.run()
