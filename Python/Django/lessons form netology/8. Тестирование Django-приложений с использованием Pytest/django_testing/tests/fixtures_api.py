import pytest
from rest_framework.test import APIClient


@pytest.fixture()
def api_client(request):
    """Фикстура для клиента API."""
    return APIClient()
