from datetime import datetime
from random import randint, choice
from urllib.parse import urljoin

from django.urls import reverse
from faker import Faker
from mimesis import Person
from mimesis.enums import Gender
from pytest import mark, param

from app.models import Product
from utils.common import Status

ORDER_BASE_URL = reverse('orders-list')
ORDER_DATE = datetime.now().date()
ORDER_TOTAL_SUM = randint(1000, 1000000)
ORDERS_COUNT = randint(5, 10)


def get_payload(user):
    """
    Generating a payload for creating/updating orders.

    We dave to explicitly Indicate the price in order to avoid further exception:
    "A field with precision 9, scale 2  must round to an absolute value less than 10^7."
    """
    payload = {
        'positions': [
            {
                "product": Product.objects.create(
                    price=randint(500, 1000).__float__(),
                    name=Person('it').surname(gender=Gender.FEMALE),
                    description=Faker('ru_RU').text(randint(50, 100))
                ).id,
                "quantity": randint(50, 100)
            }
            for _ in range(ORDERS_COUNT)
        ],
        "user": user.id
    }

    return payload


def create_order(user, session):
    """
    Creates orders.

    if we have nested structure of payload, we must to indicate <format='json'> parameter
    in session.post:
    https://stackoverflow.com/questions/66019680/django-rf-errordetail-this-field-is-required-with-apiclient
    """
    payload = get_payload(user)
    resp = session.post(ORDER_BASE_URL, payload, format='json')
    assert resp.status_code == 201


# GET

@mark.django_db
def test_list_orders(
        session_user_authorized, token_factory,
        user_factory, superuser_factory,
):
    """
    Checks getting all orders for user/superuser.
    """
    user = user_factory()
    user_token = token_factory(user=user)
    user_session = session_user_authorized(token=user_token)
    create_order(user, user_session)
    # user can not get all orders
    user_list_resp = user_session.get(ORDER_BASE_URL)
    assert user_list_resp.status_code == 403

    admin = superuser_factory()
    admin_token = token_factory(user=admin)
    admin_session = session_user_authorized(token=admin_token)
    # admin can get all orders
    admin_list_resp = admin_session.get(ORDER_BASE_URL)
    assert admin_list_resp.status_code == 200


@mark.django_db
def test_retrieve_order_through_endpoint_id(
        session_user_authorized, token_factory,
        user_factory, superuser_factory,
):
    """
    Checks retrieve specific order through endpoint <id>.
    For user/superuser.
    """
    # let's create two orders: from user and from admin
    user = user_factory()
    user_token = token_factory(user=user)
    user_session = session_user_authorized(token=user_token)
    create_order(user, user_session)

    admin = superuser_factory()
    admin_token = token_factory(user=admin)
    admin_session = session_user_authorized(token=admin_token)
    create_order(admin, admin_session)

    # receiving orders
    admin_list_resp = admin_session.get(ORDER_BASE_URL)
    assert admin_list_resp.status_code == 200
    json = admin_list_resp.json()
    user_order, admin_order = json

    # user can retrieve his order
    user_resp_ok = user_session.get(urljoin(ORDER_BASE_URL, '{}/'.format(user_order["id"])))
    assert user_resp_ok.status_code == 200
    # user can not retrieve other user order
    user_resp_failed = user_session.get(urljoin(ORDER_BASE_URL, '{}/'.format(admin_order["id"])))
    assert user_resp_failed.status_code == 403

    # admin can retrieve any orders
    for order in (user_order, admin_order):
        admin_retrieve_resp = admin_session.get(urljoin(ORDER_BASE_URL, '{}/'.format(order["id"])))
        assert admin_retrieve_resp.status_code == 200


@mark.django_db
def test_retrieve_order_through_id_user_id_status(
        session_user_authorized, token_factory,
        user_factory, superuser_factory,
):
    """
    Checks:
        retrieve specific order through url parameter <id>
        retrieve list of orders through url parameter <user_id>
        retrieve specific order through url parameter <status>
    For user/superuser.
    """
    # let's create some orders from user and receive them
    user = user_factory()
    user_token = token_factory(user=user)
    user_session = session_user_authorized(token=user_token)
    [create_order(user, user_session) for _ in range(ORDERS_COUNT)]
    admin_session = session_user_authorized(
        token=token_factory(
            user=superuser_factory()
        )
    )
    admin_list_resp = admin_session.get(ORDER_BASE_URL)
    assert admin_list_resp.status_code == 200
    json = admin_list_resp.json()

    # retrieving order via <id> url parameter
    order_id = choice(json)['id']
    payload_id = {'id': order_id}
    # user can not
    user_resp_id = user_session.get(ORDER_BASE_URL, payload_id)
    assert user_resp_id.status_code == 403
    # admin can
    admin_resp_id = admin_session.get(ORDER_BASE_URL, payload_id)
    assert admin_resp_id.status_code == 200

    # retrieving list of orders via <user_id> url parameter
    # user and admin can
    order_creator_id = user.id
    payload_creator_id = {'user_id': order_creator_id}
    user_resp_creator_id = user_session.get(ORDER_BASE_URL, payload_creator_id)
    assert user_resp_creator_id.status_code == 200
    admin_resp_creator_id = admin_session.get(ORDER_BASE_URL, payload_creator_id)
    assert admin_resp_creator_id.status_code == 200

    # retrieving list of orders via <status> url parameter
    order_status = choice(
        [Status.new.status, Status.in_progress.status, Status.done.status]
    )
    payload_status = {'status': order_status}
    # user can not
    user_resp_status = user_session.get(ORDER_BASE_URL, payload_status)
    assert user_resp_status.status_code == 403
    # admin can
    admin_resp_status = admin_session.get(ORDER_BASE_URL, payload_status)
    assert admin_resp_status.status_code == 200


@mark.parametrize('parameter_name, parameter_value', [
    param('total_sum_gte', ORDER_TOTAL_SUM, id='total_sum_gte'),
    param('total_sum_lte', ORDER_TOTAL_SUM, id='total_sum_lte'),
    param('created_at_before', ORDER_DATE, id='created_at_before'),
    param('created_at_after', ORDER_DATE, id='created_at_after'),
    param('updated_at_before', ORDER_DATE, id='updated_at_before'),
    param('updated_at_after', ORDER_DATE, id='updated_at_after'),
])
@mark.django_db
def test_retrieve_order_through_gte_lte_before_after(
        session_user_authorized, token_factory,
        user_factory, superuser_factory,
        parameter_name, parameter_value,
):
    """
    Checks retrieve orders through url parameters: 
        <total_sum>, <created_at_before>, <created_at_after>, 
        <updated_at_before>, <updated_at_after>
    For user/superuser.
    """
    # let's create some orders from user
    user = user_factory()
    user_token = token_factory(user=user)
    user_session = session_user_authorized(token=user_token)
    [create_order(user, user_session) for _ in range(ORDERS_COUNT)]
    admin_session = session_user_authorized(
        token=token_factory(
            user=superuser_factory()
        )
    )
    # user can not retrieve products via parametrize parameters
    payload = {parameter_name: parameter_value}
    user_resp = user_session.get(ORDER_BASE_URL, payload)
    assert user_resp.status_code == 403

    # admin can
    admin_resp = admin_session.get(ORDER_BASE_URL, payload)
    assert admin_resp.status_code == 200


@mark.django_db
def test_retrieve_order_through_product_name(
        session_user_authorized, token_factory,
        user_factory, superuser_factory,
):
    """
    Checks retrieve orders through url parameter <product_name>.
    For superuser.
    """
    # let's create some orders from user
    user = user_factory()
    user_token = token_factory(user=user)
    user_session = session_user_authorized(token=user_token)
    [create_order(user, user_session) for _ in range(ORDERS_COUNT)]
    admin_session = session_user_authorized(
        token=token_factory(
            user=superuser_factory()
        )
    )
    # choice random product name and id, and send request
    all_products = Product.objects.values('name', 'id')
    product = choice(all_products)
    payload = {'product_name': product['name']}
    resp = admin_session.get(ORDER_BASE_URL, payload)
    assert resp.status_code == 200

    # checking that we have received relevant orders, which contain above selected product
    json = resp.json()
    order_positions = choice(json)['positions']
    order_products_ids = [i['product'] for i in order_positions]
    assert product['id'] in order_products_ids


# POST

@mark.parametrize('is_authorized, expected_code', [
    param(True, 201, id='User authorized'),
    param(False, 401, id='User not authorized'),
])
@mark.django_db
def test_create_order(
        session_user_authorized, session_user_unauthorized,
        token_factory, user_factory, is_authorized, expected_code
):
    """
    Checks creating order. For authorised/unauthorised user.
    """
    user = user_factory()
    token = token_factory(user=user)
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    payload = get_payload(user)
    resp = session.post(ORDER_BASE_URL, payload, format='json')
    assert resp.status_code == expected_code


# PUT, PATCH

@mark.django_db
def test_update_partial_update_order(
        session_user_authorized, token_factory,
        user_factory, superuser_factory,
):
    """
    Checks update/partial_update order. For user/superuser.
    """
    # let's create two orders: from user and from admin
    user = user_factory()
    user_token = token_factory(user=user)
    user_session = session_user_authorized(token=user_token)
    create_order(user, user_session)

    admin = superuser_factory()
    admin_token = token_factory(user=admin)
    admin_session = session_user_authorized(token=admin_token)
    create_order(admin, admin_session)

    # receiving orders
    admin_list_resp = admin_session.get(ORDER_BASE_URL)
    assert admin_list_resp.status_code == 200
    json = admin_list_resp.json()
    user_order, admin_order = json

    for user_method in (user_session.put, user_session.patch):
        user_payload = get_payload(user)
        user_payload.update({"status": Status.new.status})
        user_ok_url = urljoin(ORDER_BASE_URL, '{}/'.format(user_order['id']))
        # user can change his order
        user_ok_resp = user_method(user_ok_url, user_payload, format='json')
        assert user_ok_resp.status_code == 200
        user_failed_url = urljoin(ORDER_BASE_URL, '{}/'.format(admin_order['id']))
        # user can not change other user order
        user_failed_resp = user_method(user_failed_url, user_payload, format='json')
        assert user_failed_resp.status_code == 403

        # handling the situation when user want to change status of his order
        user_payload.update({"status": Status.done.status})
        user_change_status_url = urljoin(ORDER_BASE_URL, '{}/'.format(user_order['id']))
        # user can not change status of his order
        user_change_status_resp = user_method(user_change_status_url, user_payload, format='json')
        assert user_change_status_resp.status_code == 403

    for admin_method in (admin_session.put, admin_session.patch):
        admin_payload = get_payload(admin)
        admin_payload.update({"status": Status.in_progress.status})
        # admin can change any user orders, including changing order status
        admin_url = urljoin(
            ORDER_BASE_URL, '{}/'.format(
                choice([user_order, admin_order])['id']
            )
        )
        admin_resp = admin_method(admin_url, admin_payload, format='json')
        assert admin_resp.status_code == 200


# DELETE

@mark.django_db
def test_destroy_order(
        session_user_authorized, token_factory,
        user_factory, superuser_factory,
):
    """
    Checks deleting order. For user/superuser.
    """
    # let's create two orders for user and one order for superuser
    user = user_factory()
    user_token = token_factory(user=user)
    user_session = session_user_authorized(token=user_token)
    [create_order(user, user_session) for _ in range(2)]
    admin = superuser_factory()
    admin_token = token_factory(user=admin)
    admin_session = session_user_authorized(token=admin_token)
    create_order(admin, admin_session)

    # receiving orders
    admin_list_resp = admin_session.get(ORDER_BASE_URL)
    assert admin_list_resp.status_code == 200
    json = admin_list_resp.json()
    *user_orders, admin_order = json
    user_order_1 = 0
    user_order_2 = 1

    # user can delete his order
    user_delete_user_order_url = urljoin(
        ORDER_BASE_URL, '{}/'.format(user_orders[user_order_1]['id'])
    )
    user_delete_user_order_resp = user_session.delete(user_delete_user_order_url)
    assert user_delete_user_order_resp.status_code == 204

    # user can not delete other user order
    user_delete_admin_order_url = urljoin(ORDER_BASE_URL, '{}/'.format(admin_order['id']))
    user_delete_admin_order_resp = user_session.delete(user_delete_admin_order_url)
    assert user_delete_admin_order_resp.status_code == 403

    # admin can delete any orders
    for order in (user_orders[user_order_2], admin_order):
        url = urljoin(ORDER_BASE_URL, '{}/'.format(order['id']))
        resp = admin_session.delete(url)
        assert resp.status_code == 204
