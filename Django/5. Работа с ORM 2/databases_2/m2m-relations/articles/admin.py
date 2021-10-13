from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag


class ArticleInlineFormset(BaseInlineFormSet):
    """
    Этот класс прописывается для того, чтобы потом с помощью него задать значение
    поля formset в ArticleInline.
    """
    def clean(self):
        is_main_counter = 0
        # прописываем логику, что поле с is_main:True может быть только одно, но не меньше одного
        for form in self.forms:
            is_main = form.cleaned_data.get('is_main', False)
            if is_main:
                is_main_counter += 1
        if is_main_counter > 1:
            raise ValidationError('Основной тег должен быть только один. Вы выбрали больше одного.')
        elif is_main_counter == 0:
            raise ValidationError('Как минимум 1 тег должен быть основным. Вы не выбрали ничего.')
        return super().clean()  # вызываем метод от класса BaseModelFormSet


class ArticleInline(admin.TabularInline):
    """
    Этот класс создается для того, чтобы потом в админке при создании тега
    можно было сразу прикрепить к нему статью.
    """
    model = Article.tag.through
    # где Article - модель, внутри которой реализовано m2m, tag - поле, по которому идет
    # связь, through - специальный менеджер
    extra = 1  # кол-во предлягаемых вариантов, которые выводятся по умолчанию
    formset = ArticleInlineFormset


# регистрируем наши классы Article и Tag для их отображения в админке
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]


@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
