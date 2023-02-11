POST = {
    'type': 'object',
    'properties': {
        'text': {
            'type': 'string'  # проверка типа
        },
        'visible_for': {
            'type': 'string',
            'enum': ['subsribers', 'friends', 'all']  # проверка вхождения
        },
        'priority': {
            'type': 'number',
            'minimum': 0,  # диапазон
            'maximum': 23  # диапазон
        },
        'expire_date': {
            'type': 'string',
            'pattern': '^\d{4}-\d{2}-\d{2}$'  # соответствие регулярному выражению
        }
    }
}
