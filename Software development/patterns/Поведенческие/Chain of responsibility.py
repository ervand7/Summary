"""
Этот шаблон предлагает удобный способ обработать запрос с использованием нескольких
различных методов. Каждый из них может обращаться к определенной части запроса.

Как известно, одним из лучших принципов хорошего кода является принцип единой
ответственности. Каждая часть кода должна делать одно, и только одно. Как раз
этим и занимается Цепочка обязанностей.

Например, если необходимо модифицировать некоторый контент, можно создать
различные функции-модификаторы. Каждая из них реализует один точный и четко
определенный тип модификации.
"""


def make_rstrip(value: str):
    value = value.rstrip()
    return value


def make_upper(value: str):
    value = value.upper()
    return value


def make_half(value: str):
    value = value[:len(value) // 2]
    return value.rstrip()


class ContentFilter(object):
    def __init__(self, filters=None):
        self._filters = list()
        if filters is not None:
            self._filters += filters

    def super_filter(self, content):
        for f in self._filters:
            content = f(content)
        return content


source = 'Я сегодня учу паттерны    '
my_filter = ContentFilter([
    make_rstrip,
    make_upper,
    make_half])
filtered_content = my_filter.super_filter(source)
print(filtered_content)  # Я СЕГОДНЯ У
