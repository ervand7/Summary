from django import template

register = template.Library()


@register.filter()
def up_upper(value):
    return value.upper()
