"""Здесь прописаны константы для удобства восприятия
основной логики в модуле views."""

from enum import Enum

show_counter = {'original_show': 0, 'test_show': 0}
click_counter = {'original_click': 0, 'test_click': 0}


class ABParams(Enum):
    params = ('original', 'test')

    def __init__(self, original, test):
        self.original: str = original
        self.test: str = test


class Templates(Enum):
    params = (
        'index.html',
        'landing.html',
        'landing_alternate.html',
        '404.html',
        'stats.html'
    )

    def __init__(self, index, landing, landing_alternate, error, stats):
        self.index: str = index
        self.landing: str = landing
        self.landing_alternate: str = landing_alternate
        self.error: str = error
        self.stats: str = stats
