from datetime import datetime, date
from django import template

import emoji


register = template.Library()


@register.filter
def format_bool_LTE(value):
    if value:
        return emoji.emojize(':thumbs_up:')
    return emoji.emojize(':thumbs_down:')


@register.filter
def format_date(value):
    if not isinstance(value, (date, datetime)):
        return value
    return value.strftime('%Y-%m')
