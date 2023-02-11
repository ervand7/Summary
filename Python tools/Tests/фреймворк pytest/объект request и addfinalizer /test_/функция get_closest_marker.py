import pytest


@pytest.fixture
def basedriver(request):
    print('Marker:', request.node.get_closest_marker('set1'))


@pytest.mark.set1
def test_spam(basedriver):
    assert True


def test_eggs(basedriver):
    assert True
