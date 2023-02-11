from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Phone


def show_catalog(request):
    order_by = Phone.objects.order_by
    template = 'catalog.html'
    url_parameter = request.GET.get('sort', None)
    sort_variants = {
        'sort_by_date': None,
        'sort_by_min_price': None,
        'sort_by_max_price': None,
        'sort_by_name': None
    }
    if url_parameter:
        if url_parameter == 'min_price':
            phones_from_db = order_by('price').all()
            sort_variants['by_min_price'] = True
        elif url_parameter == 'max_price':
            phones_from_db = order_by('-price').all()
            sort_variants['by_max_price'] = True
        elif url_parameter == 'name':
            phones_from_db = order_by('name').all()
            sort_variants['by_name'] = True
        else:
            phones_from_db = order_by('-release_date').all()
            sort_variants['by_date'] = True
    else:
        phones_from_db = order_by('-release_date').all()
        sort_variants['by_date'] = True
    context = {'phones': phones_from_db}
    context.update(sort_variants)
    context.update({'query_set': phones_from_db.query.__str__()})
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Phone not found')
    context = {'phone': phone}
    return render(request, template, context)
