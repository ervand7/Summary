class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        self.__counter += 1
        return self.__counter


c = Counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
