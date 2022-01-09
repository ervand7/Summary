"""
Вручную декорируем методы
"""


def cached(method):
    method_name = method.__name__

    def new_method(self):
        if method_name not in self.CACHE:
            self.CACHE[method_name] = {}
        cache = self.CACHE[method_name]

        if self._value not in cache:
            cache[self._value] = method(self)
        return cache[self._value]

    return new_method


class Number:
    CACHE = {}

    def __init__(self, value):
        self._value = value

    @cached
    def sqr(self):
        return type(self)(self._value * self._value)

    @cached
    def half(self):
        return type(self)(self._value // 2)

    def __repr__(self):
        return 'Number({value})'.format(value=self._value)


Number(10).half()
Number(20).half()
Number(30).half()
Number(40).sqr()
Number(50).sqr()

print(Number(4).CACHE)
# {'half': {10: Number(5), 20: Number(10), 30: Number(15)}, 'sqr': {40: Number(1600), 50: Number(2500)}}
