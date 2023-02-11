# источник: https://habr.com/ru/post/269759/
# В примере создания расширенной фикстуры мы передали в нее параметр request.
# Это было сделано чтобы через его метод addfinalizer добавить финализатор.
# Если необходим вызов teardown для определенной расширенной фикстуры, то можно реализовать его двумя способами:
# 1) добавив в фикстуру финализатор (через метод addfinalizer объекта request передаваемого в фикстуру
# 2) через использование конструкции yield (начиная с PyTest версии 2.4)
import pytest


@pytest.fixture(scope="function")
def resource_setup(request):
    print("resource_setup")
    print(request.fixturename)
    print(request.scope)
    print(request.function.__name__)
    print(request.cls)
    print(request.module.__name__)
    print(request.fspath)

    def resource_teardown():
        print("resource_teardown")

    request.addfinalizer(resource_teardown)


def test_1(resource_setup):
    assert True


class TestClass:
    def test_2(self, resource_setup):
        assert True


# ______________________________________________________________________________________

@pytest.yield_fixture()
def resource_setup2():
    print("resource_setup")
    yield
    print("resource_teardown")


def test_1_that_needs_resource(resource_setup2):
    print("test_1_that_needs_resource")


def test_2_that_does_not():
    print("test_2_that_does_not")


def test_3_that_does_again(resource_setup2):
    print("test_3_that_does_again")
