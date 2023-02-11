from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


catalog = {
    'car': {
        'name': 'Car',
        'description': 'это машина'
    },
    'car_1': {
        'name': 'Car',
        'description': 'это машина'
    }
}


def home_view(request):
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def info(self):
            return f'Пользователь - {self.name} возраст - {self.age}'

    data = [
        User('Bob', 19),
        User('Ray', 20),
        User('Bob', 19),
        User('Jey', 20),
        User('Wey', 19),
        User('Say', 20),
        User('Yuma', 19),
        User('Led', 20),
        User('Ney', 19),
        User('Ivan', 20),
        User('Ken', 25),
    ]
    context = {'data': data}

    return render(
        request=request, template_name='app/index.html', context=context
    )


def home_view2(request):
    data = [i for i in range(100)]
    context = {'data': data, 'datetime': datetime.now()}

    return render(request, 'app/index2.html', context=context)


def home_view3(request):
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def info(self):
            return f'Пользователь - {self.name} возраст - {self.age}'

    users = [
        User('Bob', 19),
        User('Ray', 20),
        User('Bob', 19),
        User('Jey', 20),
        User('Wey', 19),
        User('Say', 20),
        User('Yuma', 19),
        User('Led', 20),
        User('Ney', 19),
        User('Ivan', 20),
        User('Ken', 25),
    ]
    data = [i for i in range(100)]
    context = {'data': data, 'datetime': datetime.today(), 'users': users}

    return render(request, 'app/index3.html', context=context)


def home_view4(request):
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def info(self):
            return f'Пользователь - {self.name} возраст - {self.age}'

    users = [
        User('Bob', 19),
        User('Ray', 20),
        User('Bob', 19),
        User('Jey', 20),
        User('Wey', 19),
        User('Say', 20),
        User('Yuma', 19),
        User('Led', 20),
        User('Ney', 19),
        User('Ivan', 20),
        User('Ken', 25),
    ]
    data = [i for i in range(100)]
    context = {'data': data, 'datetime': datetime.today(), 'users': users}

    return render(request, 'app/home.html', context=context)


def home_view5(request):
    context = {'cars': [key for key in catalog.keys()]}

    return render(request, 'app/home2.html', context=context)


def detail_view(request, car_name):
    context = {'info': catalog.get(car_name)}

    return render(request, 'app/card.html', context=context)


def time_view(request):
    context = {'date': datetime.now()}

    return render(request, 'app/time.html', context=context)


def time_view2(request):
    context = {'date': datetime.now()}

    return render(request, 'app/time2.html', context=context)