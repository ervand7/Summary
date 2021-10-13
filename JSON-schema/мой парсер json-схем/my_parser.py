"""
Программа позволяет сравнить json-схему и ответ апи по ключам.
1) вставьте в файл json-schema.json вашу json-схему
2) вставьте в файл api_response.json ваш ответ апи из постмана
"""

import json


def parser_json_schema():
    """Возвращает ключи из json-схемы"""
    counter = []
    file = 'json-schema.json'
    with open(file) as f:
        loader = json.load(f)
        parse_object = (loader['properties'])
        for i in parse_object.keys():
            counter.append(i)

    return counter


def parser_api_response():
    """Возвращает ключи из ответа апи"""
    counter = []
    file = 'api_response.json'
    with open(file) as f:
        loader = json.load(f)
        for i in loader.keys():
            counter.append(i)

    return counter


def get_keys_absence_in_api_resp():
    """Возвращает поля, которые есть в json-схеме, но которых нет в ответе апи"""
    counter = []
    for item in parser_json_schema():
        if item not in parser_api_response():
            counter.append(item)
    return counter


def get_keys_absence_in_scheme():
    """Возвращает поля, которые есть в ответе апи, но которых нет в json-схеме"""
    counter = []
    for item in parser_api_response():
        if item not in parser_json_schema():
            counter.append(item)
    return counter


if __name__ == '__main__':
    print(len(parser_json_schema()))
    print(len(parser_api_response()))
    print(get_keys_absence_in_scheme())
    print(get_keys_absence_in_api_resp())
