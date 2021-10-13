import pytest
from model_bakery import baker
from rest_framework.authtoken.models import Token


@pytest.fixture()
def user_factory():
    """
    Creates user.
    """

    def factory(**kwargs):
        return baker.make("User", **kwargs)

    return factory


@pytest.fixture()
def superuser_factory():
    """
    Creates superuser.
    """

    def factory(**kwargs):
        return baker.make("User", **{'is_superuser': True})

    return factory


@pytest.fixture()
def token_factory():
    """
    Creates token.
    """

    def factory(**kwargs):  # kwargs: {'user': <User>}
        return Token.objects.create(**kwargs)

    return factory
