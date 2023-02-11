from django.http import HttpResponse
from django.shortcuts import render, reverse  # reverse принимает в себя некое имя
# и ищет по всем урлам эту информацию

from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    current_workdir = os.listdir()
    return HttpResponse(
        [f'{file}, ' for file in current_workdir]
    )
