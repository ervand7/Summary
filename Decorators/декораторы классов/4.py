"""
Параметризуем имя кеша (пример сложный, можно упростить и будет лучше).
"""


def mark_for_cache(method):
    method._cached = True
    return method


def make_cache(method, cache_name):
    method_name = method.__name__

    def new_method(self):
        global_cache = getattr(self, cache_name)
        if method_name not in global_cache:
            global_cache[method_name] = {}
        cache = global_cache[method_name]

        if self._value not in cache:
            cache[self._value] = method(self)
        return cache[self._value]

    return new_method


def class_decorator(cache_name):
    def inner(cls):
        setattr(cls, cache_name, {})
        for attr_name in cls.__dict__:
            attr = getattr(cls, attr_name)
            if hasattr(attr, '_cached'):
                setattr(cls, attr_name, make_cache(attr, cache_name))

        return cls

    return inner


@class_decorator('MY_CACHE')
class Number:

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

print(Number(4).MY_CACHE)
# {'half': {10: Number(5), 20: Number(10), 30: Number(15)}, 'sqr': {40: Number(1600), 50: Number(2500)}}
