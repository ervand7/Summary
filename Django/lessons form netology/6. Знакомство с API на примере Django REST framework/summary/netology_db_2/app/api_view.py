import json

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Car
from .serializers import CarSerializer, CarSerializerFromModelSerializer

GET = 'GET'
POST = 'POST'
METHODS = [GET, POST]
FIELDS = ['id', 'name']


# С помощью этого декоратора указываем методы, которые будут разрешены для данной view-функции.
# К примеру, если сделаем @api_view(http_method_names=[GET]), то уже при отправке POST-запроса
# мы в ответ получим {"detail": "Method \"POST\" not allowed."}
@api_view(http_method_names=METHODS)
def car_view(request):
    # Внимание! После приминения декоратора api_view, нам уже эта проверка на методы НЕ НУЖНА!
    # if request.method not in METHODS:
    #     # Мы сейчас хотим, чтобы эта вьюха работала по ресту и обрабатывала запросы.
    #     # Поэтому мы проверяем достоверность методов, которые к нам пришли.
    #     # Код 405 Method Not Allowed говорит нам о том, что сервер получил определенный
    #     # запрос с заданным HTTP-методом, смог его распознать, но не дает добро на его
    #     # реализацию. То есть пользователь не получит доступ к контенту, который запросил.
    #     return HttpResponse(status=405)

    if request.method == GET:
        # сейчас отправим через постман такой GET-запрос: http://localhost:8000/api/v1/cars/
        print('This was GET request')
        # ВЫДАТЬ ОТВЕТ МЫ МОЖЕМ С ПОМОЩЬЮ РАЗНЫХ ВАРИАНТОВ.
        # В первых 3 вариантах можно было бы использовать стандартный json.dumps(),
        # но мы будем использовать джанговский метод JsonResponse.

        # Вариант №1. Через генератор списков
        # cars = Car.objects.all()
        # data = [{'id': car.id, 'name': car.name} for car in cars]
        # return JsonResponse({'items': data}, status=200)

        # Вариант №2. Через джанговский метод values
        # cars = Car.objects.all().values('id', 'name')
        # # cars будет <QuerySet [{'id': 1, 'name': 'KIA'}, {'id': 2, 'name': 'LADA'}, {'id': 3, 'name': 'NIVA'}]>
        # return JsonResponse({'items': list(cars)}, status=200)

        # Вариант №3. Через values + распаковку списка, содержащего названия ключей
        # cars = Car.objects.all().values(*FIELDS)
        # # cars будет <QuerySet [{'id': 1, 'name': 'KIA'}, {'id': 2, 'name': 'LADA'}, {'id': 3, 'name': 'NIVA'}]>
        # return JsonResponse({'items': list(cars)}, status=200)

        # Вариант №4. Через DRF serializer
        cars = Car.objects.all()
        # Внимание! Поскольку из-за .all() мы передаем набор объектов, нам нужно указать флаг many=True
        serializer = CarSerializer(cars, many=True)
        return Response({'items': serializer.data},
                        status=HTTP_200_OK)  # объекты лежат в аттрибуте data; байтовый request.body нам уже не подходит

    if request.method == POST:
        print('This was POST request')
        # # ВАРИАНТ БЕЗ ИСПОЛЬЗОВАНИЯ DRF:
        # # Сейчас отправим через постман такой POST-запрос: http://localhost:8000/api/v1/cars/ с таким body: {"id": 5, "name": "NewCar"}
        # print(type(request.body), ' ', request.body)  # вот так выглядят данные до десериализации: <class 'bytes'>  b'{\n "name": "NewCAR"\n}'
        # data = json.loads(request.body)  # используем стандартный json.loads
        # print(type(data), ' ', data)   # вот так выглядят данные после десериализации: <class 'dict'>  {'name': 'NewCAR'}
        # car = Car.objects.create(**data)
        # context = {'id': car.id, 'name': car.name}
        # return JsonResponse(context, status=201)

        # ВАРИАНТ С ИСПОЛЬЗОВАНИЕМ DRF:
        # сравним request.body и request.data
        request_body = request.body  # {'key': 'value'}
        request_data = request.data  # b'{"key": "value"}'
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # raise_exception=True означает, что если объект не пройдет
        # валидацию, то сериализатор сам вернет нам нужную ошибку

        # в поле validated_data у сериализатора появляется словарь, с помощью деструктуризации которого мы можем
        # создать запись в нашу БД
        car = Car.objects.create(**serializer.validated_data)
        context = CarSerializer(car)

        return Response(context.data, status=HTTP_201_CREATED)


# ======================== 3 ВАРИАНТА РЕАЛИЗАЦИИ VIEWS НА ОСНОВЕ КЛАССОВ ========================
# ===============================================================================================
#                           1) РЕАЛИЗАЦИЯ VIEWS НА ОСНОВЕ APIView

class CarApiView(APIView):  # APIView - обязательное наследование
    def get(self, request, *args, **kwargs):  # request, *args, **kwargs - обязательные параметры
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)

        return Response({'items': serializer.data}, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car = Car.objects.create(**serializer.validated_data)
        context = CarSerializer(car)

        return Response(context.data, status=HTTP_201_CREATED)


# ===============================================================================================
#      2) РЕАЛИЗАЦИЯ VIEWS НА ОСНОВЕ ListCreateAPIView + RetrieveUpdateDestroyAPIView

class CarGetCreateApiView(ListCreateAPIView):
    """
    Этот класс получает информацию и создает информацию (get, post).
    Мы описываем, что мы достаём и в каком формате отдаём, с помощью
    атрибутов queryset и serializer.
    """
    # нужно заполнить 2 обязательных поля: queryset и serializer_class
    queryset = Car.objects.all()  # набор данных, которые мы должны получить
    serializer_class = CarSerializerFromModelSerializer  # используем продвинутый сериализатор


class CarGetPutPatchDelete(RetrieveUpdateDestroyAPIView):
    """
    Этот класс нам позволяет получить информацию по id (Retrieve),
    обновить (Update) и удалить (Destroy) (get, put, patch, delete).
    Мы описываем, что мы достаём и в каком формате отдаём, с помощью
    атрибутов queryset и serializer.
    """
    # нужно заполнить 2 обязательных поля: queryset и serializer_class
    queryset = Car.objects.all()
    serializer_class = CarSerializerFromModelSerializer


# ===============================================================================================
#                           3) РЕАЛИЗАЦИЯ VIEWS НА ОСНОВЕ ModelViewSet

class CarFromModelViewSet(ModelViewSet):
    """
    Одного этого класса достаточно, чтобы полностью реализовать GRUD.
    Мы описываем, что мы достаём и в каком формате отдаём, с помощью
    атрибутов queryset и serializer.
    """
    # нужно заполнить 2 обязательных поля: queryset и serializer_class
    queryset = Car.objects.all()
    serializer_class = CarSerializerFromModelSerializer

