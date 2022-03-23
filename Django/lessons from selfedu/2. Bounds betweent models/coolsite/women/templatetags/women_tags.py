from django import template
from women.models import *

register = template.Library()


@register.simple_tag()
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    return Category.objects.filter(pk=filter)


@register.inclusion_tag('women/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}
