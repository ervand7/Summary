from datetime import datetime, date
from django import template

register = template.Library()


@register.filter
def format_bool(value):
    if value:
        return 'Есть'
    return 'Нет'


@register.filter
def format_date(value):
    if not type(value) in [date, datetime]:
        return value
    return value.strftime('%d.%m.%Y')
