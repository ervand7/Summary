from enum import (
    Enum,
    IntEnum,
)


class Wait(Enum):
    a = (10, 1)
    b = (20, 2)
    c = (60, 0.5)
    d = (15, 2)
    e = (15, 2)
    f = (180, 2)

    def __init__(self, feature_1, feature_2):
        self.feature_1 = feature_1
        self.feature_2 = feature_2


print(Wait.b.feature_1)  # 20
print(Wait.f.feature_2)  # 2


# ____________________________________________________________________


class Friends(Enum):
    user = ('Вася.Иванов', 'слесарь')
    user2 = ('Анна.Петрова', 'врач')
    user3 = ('Семен.Кузнецов', 'водитель')
    user4 = ('Виктор.Смирнов', 'учитель')

    def __init__(self, pr, ru):
        self.pr: str = pr
        self.ru: str = ru


print(Friends.user2.ru)  # врач
print(Friends.user4.pr)  # Виктор.Смирнов
