from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):  # рекомендуется все функции называть с окончанием view
    rez = 2 + 3
    return HttpResponse(f'Привет Django {rez}')
