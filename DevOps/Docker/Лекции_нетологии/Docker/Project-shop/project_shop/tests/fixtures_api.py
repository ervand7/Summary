import pytest
from rest_framework.test import APIClient


@pytest.fixture()
def session_user_authorized(request):
    """
    Returns authorized user.
    """
    def inner(token):
        session = APIClient()
        session.credentials(HTTP_AUTHORIZATION="Token %s" % token)
        return session
    return inner


@pytest.fixture()
def session_user_unauthorized(request):
    """
    Returns unauthorized user.
    """
    return APIClient()
