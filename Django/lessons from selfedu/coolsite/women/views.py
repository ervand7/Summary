from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Women

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):  # request = HttpRequest
    posts = Women.objects.all()
    return render(
        request,
        template_name='women/my_index.html',
        context=dict(title='Главная страница', menu=menu, posts=posts))


def about(request):  # request = HttpRequest
    return render(
        request, template_name='women/about.html',
        context=dict(title='О сайте', menu=menu))


def categories(request, cat):
    a = request.GET
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{cat}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
