from django.db import models


class CountryChoices(models.TextChoices):
    RUSSIA = 'RUS', 'Россия'
    UKRAINE = 'UKR', 'Украина'
    UK = 'UK', 'Великобритания'
    SPAIN = 'SP', 'Испания'
    BRAZIL = 'BR', 'Бразилия'


class Player(models.Model):  # обязательное наследование
    # Мы можем не указывать первичный ключ у этой модели. По умолчанию Django создает его
    # Если же мы все таки хотим задать свой первичный ключ, то это делается так:
    # address = models.TextField(primary_key=True)

    # значения полей тоже должны браться из models
    name = models.TextField()

    country = models.TextField(default='', choices=CountryChoices.choices)

    team = models.ForeignKey(
        'Team',  # указываем строкой, чтобы не было ошибки, так как класс Team объявлен ниже. Это задумка Django
        null=True,  # null=True позволит не заполнять это поле в БД
        blank=True,  # это ограничение не на уровне БД, а на уровне Django,
        # оно означает, что данный атрибут необязателен к заполнению. По умолчанию все поля обязательны
        on_delete=models.CASCADE  # on_delete - это обязательное поле. Если мы указываем ForeignKey
        # эта конструкция говорит о том, что делать с моделью, если удаляется ForeignKey,
        # на который модель ссылается. Эта конструкция работает на уровне Django, а не БД
        # CASCADE - автоматически удаляет строку из зависимой таблицы
        # также нужно знать, что Django автоматически навешивает индексы на все ForeignKey
        # то есть в БД этот ForeignKey будет players_player_team_id_c95b0652
        # Плюс к этому в БД в таблице эта колонка будет именоваться как team_id, потому что она ForeignKey
    )

    def __str__(self):
        return f'{self.id}: {self.name}'


class Team(models.Model):
    name = models.TextField()

    country = models.TextField(default='', choices=CountryChoices.choices)

    def __str__(self):
        return f'{self.id}: {self.name}'