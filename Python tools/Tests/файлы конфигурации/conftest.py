# про сложные conftest.py читать здесь: https://pytest-docs-ru.readthedocs.io/ru/latest/example/markers.html#mark-run
import pytest
import smtplib

"""
Если вы планируете использовать фикстуру в нескольких тестах, то можно объявить
ее в файле conftest.py.
При этом импортировать ее не нужно - pytest найдет ее автоматически.
Поиск фикстур начинается с тестовых классов,
затем они иущется в тестовых модулях и в файлах conftest.py, и, в
последнюю очередь, во встроенных и сторонних плагинах.
"""


# В следующем примере мы помещаем фикстуру в файл conftest.py, чтобы доступ к ней могли иметь
# разные тесты из разных тестовых модулей нашего каталога:


@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


"""
Наша фикстура по-прежнему называется smtp_connection, и получить к ней доступ из 
любой тестовой функции или другой фикстуры (в пределах директории, в которой 
расположен наш файл conftest.py и ее поддиректорий) можно, передав параметр 
smtp_connection в объявлении нашей функции/фикстуры:
"""


# Вот пример использования addfinalizer для разрыва соединения в фикстуре smtp_connection:


@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()

    request.addfinalizer(fin)
    return smtp_connection  # возвращает значение фикстуры
