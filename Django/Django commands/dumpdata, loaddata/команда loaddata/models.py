from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название статьи')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tag = models.ManyToManyField('Tag', related_name='articles', through='TagInArticle')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class TagInArticle(models.Model):
    article = models.ForeignKey(Article, verbose_name='Article', on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, verbose_name='Tag', on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной тег', default=False)  # default=False означает,
    # что по умолчанию все теги у нас будут не основными

    def __str__(self):
        return f'{self.id} - {self.article} | {self.tag}'
