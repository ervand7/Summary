def create_is_main_field(selection, article_id_tag_id_is_main):
    """
    Функция создает поле <is_main> для тегов в статьях.

    :param selection: <QuerySet> - подготовленная выборка, которая затем пойдет в шаблон
    :param article_id_tag_id_is_main: list - список со словарями.
        Пример словаря: {'article_id': n, 'tag_id': n, 'is_main': Bool}
    """
    selection_as_dicts = [s for s in selection]
    for article in selection_as_dicts:
        # создаем каунтер, где для каждой статьи будет собираться {tag_id: is_main} ее тегов
        article.tags_counter = []
        for dct in article_id_tag_id_is_main:
            if article.id == dct['article_id']:
                article.tags_counter.append({dct['tag_id']: dct['is_main']})

        # создаем во всех тегах поле is_main и присваиваем ему соответствующее значение
        for tag in article.tag.all():
            for tag_id_is_main in article.tags_counter:
                if tag.id in tag_id_is_main.keys():
                    tag.is_main = tag_id_is_main[tag.id]


def sort_tags(selection):
    """
    Функция сортирует теги.

    В списке тегов главный тег должен идти первым, а затем все остальные в алфавитном порядке.
    :param selection: <QuerySet> - подготовленная выборка, которая затем пойдет в шаблон
    """
    for article in selection:
        first_main_tag = None
        other_tags = []
        for tag in article.tag.all():
            if tag.is_main:
                first_main_tag = tag
            else:
                other_tags.append(tag)
        # создаем вспомогательный словарь, по которому далее будем сортировать все теги,
        # которые не относятся к главному. Где ключ - имя тега, значение - тег
        dict_sort_other_tags = {}
        for o_t in other_tags:
            dict_sort_other_tags[o_t.name] = o_t
        list_sort_other_tags = sorted(dict_sort_other_tags.items(), key=lambda x: x[0])
        sorted_other_tags = [tag_info[1] for tag_info in list_sort_other_tags]
        # создаем для статей поле sorted_tags, по которому далее будут выводиться теги в шаблоне
        article.sorted_tags = [first_main_tag] + sorted_other_tags
