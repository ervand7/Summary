from random import randint, choice
from urllib.parse import urljoin

from django.urls import reverse
from faker import Faker
from mimesis import Person
from mimesis.enums import Gender
from pytest import mark, param

from app.models import Product

PRODUCT_BASE_URL = reverse('products-list')
PRODUCTS_BIG_QUANTITY = randint(50, 100)
PRODUCT_PRICE = randint(500, 1000).__float__()
PRODUCT_NAME = Person('it').surname(gender=Gender.FEMALE)
PRODUCT_DESCRIPTION = Faker('ru_RU').text(randint(500, 1000))


# GET

@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.django_db
def test_list_products(
        session_user_authorized, session_user_unauthorized, 
        product_factory, token_factory,
        user_factory, is_authorized
):
    """
    Checks getting all products for authorized/unauthorized user.
    """
    user = user_factory()
    token = token_factory(user=user)
    product_factory(_quantity=PRODUCTS_BIG_QUANTITY)
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    response = session.get(PRODUCT_BASE_URL)
    assert response.status_code == 200
    assert len(response.json()) == PRODUCTS_BIG_QUANTITY


@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.django_db
def test_retrieve_product_through_id_endpoint(
        session_user_authorized, session_user_unauthorized,
        product_factory, token_factory,
        user_factory, is_authorized
):
    """
    Checks getting specific product through endpoint id.
    For authorized/unauthorized user.
    """
    user = user_factory()
    token = token_factory(user=user)
    product_factory(_quantity=PRODUCTS_BIG_QUANTITY)
    product_id = choice(Product.objects.values_list('id', flat=True))
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    url = urljoin(PRODUCT_BASE_URL, f'{product_id}/')
    response = session.get(url)
    assert response.status_code == 200


@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.django_db
def test_retrieve_product_through_id_parameter(
        session_user_authorized, session_user_unauthorized,
        product_factory, token_factory,
        user_factory, is_authorized
):
    """
    Checks getting specific product through url parameter id.
    For authorized/unauthorized user.
    """
    user = user_factory()
    token = token_factory(user=user)
    product_factory(_quantity=PRODUCTS_BIG_QUANTITY)
    product_id = choice(Product.objects.values_list('id', flat=True))
    payload = {'id': product_id}
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    response = session.get(PRODUCT_BASE_URL, payload)
    assert response.status_code == 200


@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.parametrize('price_filter', [
    param('price_gte', id='Price greater than'),
    param('price_lte', id='Price less than'),
])
@mark.django_db
def test_retrieve_product_through_price_parameter(
        session_user_authorized, session_user_unauthorized,
        product_factory, token_factory,
        user_factory, is_authorized, price_filter
):
    """
    Checks getting specific product through url parameter price.
    For authorized/unauthorized user.
    """
    user = user_factory()
    token = token_factory(user=user)
    product_factory(_quantity=PRODUCTS_BIG_QUANTITY)
    payload = {price_filter: PRODUCT_PRICE}
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    response = session.get(PRODUCT_BASE_URL, payload)
    assert response.status_code == 200


@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.parametrize('name_or_description', [
    param('name', id='Name icontains'),
    param('description', id='Description icontains'),
])
@mark.django_db
def test_retrieve_product_through_name_or_description_parameter(
        session_user_authorized, session_user_unauthorized,
        product_factory, token_factory,
        user_factory, is_authorized, name_or_description
):
    """
    Checks getting specific product through url parameter name or description
    (depending on the parametrization). For authorized/unauthorized user.
    """
    user = user_factory()
    token = token_factory(user=user)
    product_factory(_quantity=PRODUCTS_BIG_QUANTITY)
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    common_response = session.get(PRODUCT_BASE_URL)
    assert common_response.status_code == 200
    initial_letters = \
        choice(common_response.json())[name_or_description][:randint(5, 10)]
    payload = {name_or_description: initial_letters}
    detailed_response = session.get(PRODUCT_BASE_URL, payload)
    assert detailed_response.status_code == 200
    assert detailed_response.json()[0][name_or_description].startswith(initial_letters)


# POST

@mark.parametrize('is_superuser, expected_status_code', [
    param(True, 201, id='Is superuser'),
    param(False, 403, id='Is not superuser'),
])
@mark.django_db
def test_create_product(
        session_user_authorized, product_factory, token_factory,
        user_factory, superuser_factory, is_superuser, expected_status_code,
):
    """
    Checks possibility of creating product for user/superuser.
    """
    user = superuser_factory() if is_superuser else user_factory()
    token = token_factory(user=user)
    session = session_user_authorized(token=token)
    payload = {
        "name": PRODUCT_NAME,
        "description": PRODUCT_DESCRIPTION,
        "price": PRODUCT_PRICE
    }
    response = session.post(PRODUCT_BASE_URL, payload)
    assert response.status_code == expected_status_code


# PUT, PATCH

@mark.parametrize('param_method', [
    param('PUT', id='PUT METHOD'),
    param('PATCH', id='PATCH METHOD'),
])
@mark.parametrize('is_superuser, expected_status_code', [
    param(True, 200, id='Is superuser'),
    param(False, 403, id='Is not superuser'),
])
@mark.django_db
def test_update_partial_update_product(
        session_user_authorized, product_factory, token_factory,
        user_factory, superuser_factory, param_method,
        is_superuser, expected_status_code
):
    """
    Checks possibility of update/partial_update product for user/superuser.
    """
    user = superuser_factory() if is_superuser else user_factory()
    token = token_factory(user=user)
    session = session_user_authorized(token=token)
    product_factory(_quantity=PRODUCTS_BIG_QUANTITY)
    product_id = choice(Product.objects.values_list('id', flat=True))
    get_url = urljoin(PRODUCT_BASE_URL, f'{product_id}/')
    get_response = session.get(get_url)
    assert get_response.status_code == 200

    payload = {
        "id": product_id,
        "name": PRODUCT_NAME,
        "description": PRODUCT_DESCRIPTION,
        "price": PRODUCT_PRICE
    }
    request_method = session.put if param_method == 'PUT' else session.patch
    product_change_url = urljoin(PRODUCT_BASE_URL, f'{product_id}/')
    product_change_response = request_method(product_change_url, payload)
    assert product_change_response.status_code == expected_status_code


# DELETE

@mark.parametrize('is_superuser, expected_while_delete, expected_after_delete', [
    param(True, 204, 404, id='Is superuser'),
    param(False, 403, 200, id='Is not superuser'),
])
@mark.django_db
def test_destroy_product(
        session_user_authorized, product_factory, token_factory,
        user_factory, superuser_factory, is_superuser,
        expected_while_delete, expected_after_delete
):
    """
    Checks possibility of delete product for user/superuser.
    """
    user = superuser_factory() if is_superuser else user_factory()
    token = token_factory(user=user)
    session = session_user_authorized(token=token)
    product_factory(_quantity=PRODUCTS_BIG_QUANTITY)
    product_id = choice(Product.objects.values_list('id', flat=True))
    get_url = urljoin(PRODUCT_BASE_URL, f'{product_id}/')
    get_response = session.get(get_url)
    assert get_response.status_code == 200

    delete_url = urljoin(PRODUCT_BASE_URL, f'{product_id}/')
    delete_response = session.delete(delete_url)
    assert delete_response.status_code == expected_while_delete

    get_deleted_product_url = urljoin(PRODUCT_BASE_URL, f'{product_id}/')
    response_get_deleted_product = session.get(get_deleted_product_url)
    assert response_get_deleted_product.status_code == expected_after_delete
