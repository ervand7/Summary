from django_filters import rest_framework as filters

from advertisements.models import Advertisement, STATUS_CHOICES


class AdvertisementFilter(filters.FilterSet):
    """
    Фильтры для объявлений.
    Запрос без фильтров выглядит так: GET http://localhost:4000/api/v1/advertisements/
    """

    id = filters.ModelMultipleChoiceFilter(
        to_field_name="id", queryset=Advertisement.objects.all()
    )
    # DateFromToRangeFilter потом сам добавит (в урле) окончания _before и _after к нашему created_at
    # http://127.0.0.1:4000/api/v1/advertisements/?created_at_before=2021-07-16
    # http://127.0.0.1:4000/api/v1/advertisements/?created_at_after=2021-07-18
    created_at = filters.DateFromToRangeFilter()
    # http://127.0.0.1:4000/api/v1/advertisements/?status=CLOSED
    # http://127.0.0.1:4000/api/v1/advertisements/?status=OPEN
    status = filters.ChoiceFilter(choices=STATUS_CHOICES)
    # http://127.0.0.1:4000/api/v1/advertisements/?creator=1
    creator = filters.ModelMultipleChoiceFilter(
        to_field_name="creator_id", queryset=Advertisement.objects.all()
    )
    # Пример комбинированного запроса (создатель и дата)
    # http://127.0.0.1:4000/api/v1/advertisements/?creator=1&created_at_after=2021-07-18

    # заполняем обязательный подкласс Meta
    class Meta:
        model = Advertisement
        # используем fields, чтобы избежать фильтров, которые могут сгенерироваться автоматически
        fields = ("id", "created_at", "status", "creator")
