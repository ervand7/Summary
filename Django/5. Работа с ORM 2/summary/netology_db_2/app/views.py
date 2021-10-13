from django.shortcuts import render

from app.models import CarShop, Car


def create_shops_view(request):
    fixture = [
        {'name': 'Магазин 1'},
        {'name': 'Магазин 2'}
    ]
    # ниже мы будем использовать деструктуризатор словаря (**). Так что в этой фикстуре название
    # ключа должно совпадать с названием поля <name> из модели CarShop. Так как распаковка будет именно по ключу.

    for shop in fixture:
        # CarShop.objects.create(name=shop['name'])  # так мы могли бы создать объект в БД
        # CarShop.objects.create(**shop)  # или равнозначным таким способом через деструктуризацию словаря
        # но так у нас не проверяется if exists. Поэтому мы используем update_or_create
        CarShop.objects.update_or_create(defaults=shop, **shop)  # defaults= - обязательный параметр

    context = {'shops': CarShop.objects.all()}

    return render(request, template_name='app/carShop.html', context=context)


def create_cars_view(request):
    fixture = [
        {'name': 'Машина 1'},
        {'name': 'Машина 2'},
        {'name': 'Машина 3'},
        {'name': 'Машина 4'}
    ]

    for car in fixture:
        Car.objects.update_or_create(defaults=car, **car)

    context = {'cars': Car.objects.all()}

    return render(request, template_name='app/cars.html', context=context)


def add_cars_to_shop_view(request):
    """Именно в этой функции и будет осуществлена связь m2m."""
    cars = Car.objects.all()
    shops_before = CarShop.objects.all()  # магазины, в которых еще не добавлены машины

    # добавляем машины в магазины
    for shop in shops_before:
        for car in cars:
            shop.car.add(car)  # shop.car - это поле m2m из CarShop
            # shop.car.remove(car)  # еще один возможный метод

    shops_after = CarShop.objects.all()  # те же магазины, но уже в них добавлены машины
    for shop in shops_after:
        # В shop.car сейчас должны содержаться автомобили, которые мы ранее добавили
        # print(f'{shop} - {shop.car}')  # так в shop.car получим app.Car.None и данные из БД не выведутся в консоль
        # print(f'{shop} - {shop.car.all()}')  # так тоже можно было сделать, но мы используем filter
        # так как, раз у нас есть all(), значит тут мы можем при необходимости применить и другие фильтры
        print(f'{shop} - {shop.car.filter(id__lt=2)}')

    # выведем в консоль все магазины, в которых продается наша (конкретно первая) машина
    # сравни:
    #     [shop.car.all() for shop in CarShop.objects.all()] - так получаем из каждого магазина все машины
    #     x = Car.objects.first().shops.all() - так получаем для первой машины все ее магазины, в которых она продается
    first_car_magazines = Car.objects.first().shops.all()  # shops берется из related_name (models.py, 10 строка)
    print(first_car_magazines)
    # Car.objects.first().carshop_set.all() если не прописывать related_name в классе CarShop
# то есть принцип такой: после Car.objects.first(). прописываем lowercase класс CarShop и приписываем к нему _set.all()

    context = {'shops': CarShop.objects.all()}
    # context = {'shops': CarShop.objects.all().prefetch_related('car')}
    # context = {'shops': CarShop.objects.all().values('id')}  # [{'id': 3}, {'id': 1}, {'id': 2}]
    # context = {'shops': CarShop.objects.all().values_list('name', flat=True)} #['Магазин 3', 'Магазин 1', 'Магазин 2']

    print(context)

    return render(request, 'app/carShop.html', context=context)

