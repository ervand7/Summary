from .consts import show_counter, click_counter


def get_conversion():
    """Функция делит кол-во переходов
    (на главную страницу с лендингов original и test)
    на кол-во отображений страниц (original и test)."""

    test_conv, original_conv = 0, 0
    try:
        test_conv = round(
            click_counter['test_click'] / show_counter['test_show'], 1
        )
        original_conv = round(
            click_counter['original_click'] / show_counter['original_show'], 1
        )
    except ZeroDivisionError:
        ...
    return test_conv, original_conv
