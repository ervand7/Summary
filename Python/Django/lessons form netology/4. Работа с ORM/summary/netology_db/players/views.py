from django.shortcuts import render

from players.models import Player


def list_players(request):
    template_name = 'players/list_players.html'
    context = {}
    players_query = Player.objects.select_related('team')  # сохраняем в переменную players вывод всех данных из модели
    # objects это менеджер для запросов. У меня не получается по нему провалиться в документацию,
    # но мы можем перейти сюда через поиск command+shift+f: class Manager(BaseManager.from_queryset(QuerySet)):
    # и это будет результатом проваливания в документацию
    # Player.objects.all - значит получить все объекты (не фильтровать)
    name_filter = request.GET.get('name')
    if name_filter:
        players_query = players_query.filter(name__icontains=name_filter)

    context['players'] = players_query
    return render(request, template_name, context)
