from django import template

register = template.Library()


@register.filter
def get_dict_value(horizon_row_as_dict: dict, key: str) -> str:
    """Attention! In template the first parameter will go to
    function by default."""
    return horizon_row_as_dict[key]


@register.filter
def convert_str_to_float(indicator: str) -> float:
    """
    Initial type of indicators is str. We need
    float if indicator else ''
    """
    rez = float(indicator) if indicator else ...
    return rez