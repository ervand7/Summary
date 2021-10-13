import math
from urllib.parse import urlencode

from django.conf import settings
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, reverse
from datetime import datetime


def admin_email_view(request):
    email = settings.ADMIN_EMAIL
    return HttpResponse(f"Админская почта - {email}")


def name_info_view(request):
    data = {
        'Ivan': 'руководитель отдела разработки',
        'Alex': 'руководитель отдела тестирования',
    }
    name = request.GET.get('ervand', None)  # вся инфо из адресной строки находится в словаре GET
    return HttpResponse(f'Пользователь {name} - {data.get(name, "не найден")}')


def old_date_view(request, year, month, day):
    date = datetime(year, month, day)
    return HttpResponse(date)


def date_view(request, value):
    return HttpResponse(value)


CONTENT = [str(i) for i in range(1000)]


def old_pagi_view(request):  # это наш собственный пагинатор
    page = int(request.GET.get('page', 1))
    element_per_page = 10
    content = CONTENT[page * element_per_page: element_per_page * (page + 1)]
    return HttpResponse('<br>'.join(content))


def pagi_view(request):
    default_page_number = 1
    page_number = int(request.GET.get('page', default_page_number))
    if page_number <= 0:
        page_number = default_page_number

    element_per_page = 10
    paginator = Paginator(CONTENT, element_per_page)
    page = paginator.get_page(page_number)  # так получаем всю информацию о странице
    content = page.object_list  # так получаем содержимое текущей страницы
    if page.has_next():
        next_page = page.next_page_number()
    if page.has_previous():
        previous_page = page.previous_page_number()
    num_pages = paginator.num_pages
    return HttpResponse('<br>'.join(content))


def add_pagi_view(request):
    template_name = 'app/index.html'

    default_page_number = 1
    page_number = int(request.GET.get('page', default_page_number))
    if page_number <= 0:
        page_number = default_page_number

    element_per_page = 10
    paginator = Paginator(CONTENT, element_per_page)
    page = paginator.get_page(page_number)  # так получаем всю информацию о странице
    next_page = page.next_page_number()
    previous_page = page.previous_page_number()

    context = {
        'current_page': page_number,
        'next_page': next_page,
        'prev_page': previous_page,
        'article': CONTENT
    }
    return render(request, template_name, context)

