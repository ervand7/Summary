from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.order_by('price').select_related(
        'phonesamsung', 'phoneapple', 'phonenokia'
    )
    context = {'phones': phones}
    return render(request, template, context)
