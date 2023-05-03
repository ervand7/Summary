"""
Автоматически декорируем помеченные методы (без хардкода).
"""


def mark_for_cache(method):
    method._cached = True
    return method


def make_cache(method):
    method_name = method.__name__

    def new_method(cls):
        if method_name not in cls.CACHE:
            cls.CACHE[method_name] = {}

        if cls._value not in cls.CACHE[method_name]:
            cls.CACHE[method_name][cls._value] = method(cls)
        return cls.CACHE[method_name][cls._value]

    return new_method


def cached_methods(cls):
    for attr_name in cls.__dict__:
        attr = getattr(cls, attr_name)
        if hasattr(attr, '_cached'):
            setattr(cls, attr_name, make_cache(attr))

    return cls


@cached_methods
class Number:
    CACHE = {}

    def __init__(self, value):
        self._value = value

    @mark_for_cache
    def sqr(self):
        return type(self)(self._value * self._value)

    @mark_for_cache
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
