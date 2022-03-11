import pytest
from model_bakery import baker


@pytest.fixture()
def student_factory():
    def factory(**kwargs):
        return baker.make("Student", **kwargs)
    return factory
