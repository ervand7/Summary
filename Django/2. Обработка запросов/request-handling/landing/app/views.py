from .consts import (
    ABParams, Templates, show_counter, click_counter
)
from .rendered_logic import get_conversion

from django.shortcuts import render


def index(request):
    """Функция подсчитывает клики (на original и test) и
    отвечает за отображение главной страницы."""

    ab_parameter = request.GET.get('from-landing')
    if ab_parameter == ABParams.params.original:
        click_counter['original_click'] += 1
    elif ab_parameter == ABParams.params.test:
        click_counter['test_click'] += 1

    return render(
        request=request, 
        template_name=Templates.params.index
    )


def landing(request):
    """Функция подсчитывает кол-во переходов на
     страницы original и test, а также отвечает за
    отображение этих страниц."""

    ab_parameter = request.GET.get('ab-test-arg')
    if ab_parameter == ABParams.params.original:
        template = Templates.params.landing
        show_counter['original_show'] += 1
    elif ab_parameter == ABParams.params.test:
        template = Templates.params.landing_alternate
        show_counter['test_show'] += 1
    else:
        template = Templates.params.error

    return render(
        request=request, 
        template_name=template
    )


def stats(request):
    """Функция отвечает за отображение страницы о статистикой"""
    test_conversion = get_conversion()[0]
    original_conversion = get_conversion()[1]
    context = {
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    }
    
    return render(
        request=request,
        template_name=Templates.params.stats,
        context=context
    )
