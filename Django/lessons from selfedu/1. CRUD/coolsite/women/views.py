from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


def index(request):  # request = HttpRequest
    return HttpResponse('Страница приложения Women')


def categories(request, cat):
    a = request.GET
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{cat}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
