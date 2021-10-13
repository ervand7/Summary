import pytest
from model_bakery import baker


@pytest.fixture()
def course_factory():
    def factory(**kwargs):
        return baker.make("Course", **kwargs)
    return factory

