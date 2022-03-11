from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.custom_permissions import IsCreator, IsAdmin
from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """
    ViewSet для объявлений.

    Поскольку наш вью-класс наследуется от ModelViewSet, мы должны заполнить
    4 обязательных поля: queryset, serializer_class, filter_backends и filterset_class.
    Далее, уже под капотом, ModelViewSet распарсит эти поля.
    """
    # следующие 3 аттрибута оверрайдятся из GenericApiView
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """
        Функция определения прав для действий.
        Внимание! Здесь мы оверрайдим родительский метод get_permissions

        Обрабатываем права доступа, чтобы в противном случае возвращались:
        Response code: 401 (Unauthorized): <Authentication credentials were not provided>
        или
        Response code: 403 (Forbidden): <You do not have permission to perform this action>
        """
        if self.action in ["update", "partial_update", "destroy"] \
                and self.request.user.is_superuser:
            return [IsAdmin()]

        else:
            if self.action in ["create"]:
                return [IsAuthenticated()]
            elif self.action in ["update", "partial_update", "destroy"]:
                return [IsCreator()]  # IsCreator проверяет и аунтефикацию под своим капотом
            return []
