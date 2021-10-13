from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView

from .models import Car
from .serializers import CarSerializerFromModelSerializer, z


# =========================================================================================
# =========================================================================================
# ================================== Ф И Л Ь Т Р А Ц И Я ==================================
# ВАРИАНТ 1. С ОПРЕДЕЛЕНИЕМ КЛАССА ФИЛЬТРАЦИИ
class CarFilter(filters.FilterSet):
    """
    Класс для определения фильтров. Тут мы прописываем возможные параметры для
    фильтрации под каждое поле модели.
    """
    # зададим 3 кастомных фильтра: id, amount_from и amount_to
    # это будут те поля, которые будут присутствовать в урле
    # http://127.0.0.1:4000/api/v1/cars/?id=3
    id = filters.ModelMultipleChoiceFilter(to_field_name="id", queryset=Car.objects.all())
    # http://127.0.0.1:4000/api/v1/cars/?amount_from=350
    amount_from = filters.NumberFilter(field_name="amount", lookup_expr="gte")  # lookup_expr - параметр фильтрации
    # то есть в БД фильтрация будет идти по <gte>
    # http://127.0.0.1:4000/api/v1/cars/?amount_to=350
    amount_to = filters.NumberFilter(field_name="amount", lookup_expr="lte")

    class Meta:
        # тут мы должны заполнить 2 обязательных поля: model и fields
        model = Car
        fields = ("id", "amount_from", "amount_to",)


class CarViewSetVariant1(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializerFromModelSerializer
    # filter_backends, filterset_class - заразервирванные имена
    filter_backends = [DjangoFilterBackend]  # DjangoFilterBackend исполняет роль фильтрующего бекэнда
    filterset_class = CarFilter  # CarFilter - класс с прописанными фильтрами, который мы прописали выше


# ===============================================================================
# ВАРИАНТ 2. БЕЗ ОПРЕДЕЛЕНИЯ КЛАССА ФИЛЬТРАЦИИ

class CarViewSetVariant2(viewsets.ModelViewSet):
    """
    https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html#using-the-filterset-fields-shortcut
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializerFromModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'amount']
    # http://127.0.0.1:4000/api/v1/cars/?name=first_car
    # http://127.0.0.1:4000/api/v1/cars/?amount=300


# ===============================================================================
# ВАРИАНТ 3. БЕЗ ИСПОЛЬЗОВАНИЯ БИБЛИОТЕКИ django_filters. ПОЛНОСТЬЮ КАСТОМНЫЙ ПУТЬ

class CarViewSetVariant3(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializerFromModelSerializer
    # filter_backends, filterset_fields - зарезервированные имена
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'amount']

    def get_queryset(self):
        """
        Переопределяем get_queryset родительского класса.
        """
        queryset = super().get_queryset()
        amount = self.request.query_params.get('amount')
        if amount:
            queryset = queryset.filter(amount=amount)
        # http://127.0.0.1:4000/api/v1/cars/?amount=2
        return queryset


# =========================================================================================
# =========================================================================================
# ============================ В А Л И Д А Ц И Я. Сохранение ==============================
class CarViewSet(viewsets.ViewSet):
    """
    В DRF принято описывать сохранение данных в сериализаторе.
    Валидация данных и сохранение будет выполняться автоматически, если использовать
    ModelViewSet. В противном случае можно сохранить модель явно, как представленно ниже.

    Обратите внимание, что create — это метод ViewSet, который вызывается при POST-запросе.
    При PATCH/PUT будет вызываться метод update. Подробнее в документации про
    ModelViewSet: https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    """

    # Внимание! Все это мы прописываем только в том случае, если не используем ModelViewSet
    # В данном случае мы используем просто ViewSet.
    def create(self, request, *args, **kwargs):  # request, *args, **kwargs - обязательные параметры
        serializer = CarSerializerFromModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # внутри save находится множетво ассертов
        cars = Car.objects.create(**serializer.validated_data)
        context = CarSerializerFromModelSerializer(cars)

        return Response(context.data, status=HTTP_201_CREATED)
    # POST http://localhost:4000/api/v1/cars/
    # with body: {"name": "234", "amount":  1234, "password": "qwert", "password_confirm": "qwert"}


# =========================================================================================
# =========================================================================================
# ============================== А У Т Е Н Т И Ф К А Ц И Я ================================
class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

# =========================================================================================
# =========================================================================================
# ============================== А В Т О Р И З А Ц И Я ====================================

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Вы успешно вышли', status=200)
