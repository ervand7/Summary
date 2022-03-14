from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Women

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):  # request = HttpRequest
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(
        request,
        template_name='women/my_index.html',
        context=context)


def about(request):  # request = HttpRequest
    return render(
        request, template_name='women/about.html',
        context=dict(title='О сайте', menu=menu))


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def categories(request, cat):
    a = request.GET
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{cat}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
