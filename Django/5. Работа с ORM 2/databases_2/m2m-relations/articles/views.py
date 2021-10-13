from django.shortcuts import render

from .calculate_logic import create_is_main_field, sort_tags
from .models import Article, Tag, TagInArticle


def articles_list_view(request):
    # подготовим данные для загрузки в БД в таблицу Tag
    db_load_tags = [
        {'name': 'Культура'},
        {'name': 'Город'},
        {'name': 'Здоровье'},
        {'name': 'Космос'},
        {'name': 'Международные отношения'},
        {'name': 'Наука'}
    ]
    for tag in db_load_tags:
        Tag.objects.update_or_create(defaults=tag, **tag)  # используем деструктуризацию словаря

    # так будет выглядесь выборка, которая пойдет в шаблон
    selection = Article.objects.order_by('-published_at').all().prefetch_related('tag')
    # получаем нужные нам данные для дальнейшей работы
    tags_description = TagInArticle.objects.all().values('article_id', 'tag_id', 'is_main')
    article_id_tag_id_is_main = [t_d for t_d in tags_description]

    create_is_main_field(
        selection=selection, article_id_tag_id_is_main=article_id_tag_id_is_main
    )
    sort_tags(selection=selection)
    context = {'articles': selection}

    return render(request=request, template_name='articles/news.html', context=context)
