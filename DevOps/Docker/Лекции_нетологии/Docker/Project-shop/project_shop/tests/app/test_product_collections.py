from random import randint, choice
from urllib.parse import urljoin

from django.urls import reverse
from faker import Faker
from mimesis import Person
from mimesis.enums import Gender
from pytest import mark, param

from app.models import Product

COLLECTION_BASE_URL = reverse('product-collections-list')
COLLECTIONS_COUNT = randint(2, 5)

PRODUCT_COUNT = randint(5, 10)


def get_payload():
    """
    Generate payload for collection creating.
    """
    payload = {
        "header": Faker('ru_RU').text(randint(50, 100)),
        "text": Faker('ru_RU').text(randint(200, 1000)),
        "products": [
            Product.objects.create(
                price=randint(500, 1000).__float__(),
                name=Person('it').surname(gender=Gender.FEMALE),
                description=Faker('ru_RU').text(randint(50, 100))
            ).id
            for _ in range(PRODUCT_COUNT)
        ]
    }

    return payload


def create_collection(session):
    """
    Creates collection.
    """
    payload = get_payload()
    resp = session.post(COLLECTION_BASE_URL, payload, format='json')
    assert resp.status_code == 201


# GET

@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.django_db
def test_list_collections(
        session_user_authorized, session_user_unauthorized,
        user_factory, superuser_factory, token_factory, is_authorized
):
    """
    Checks getting all collections. For authorised/unauthorised user.
    """
    # let's create some collections
    admin = superuser_factory()
    admin_token = token_factory(user=admin)
    admin_session = session_user_authorized(token=admin_token)
    [create_collection(admin_session) for _ in range(COLLECTIONS_COUNT)]

    user = user_factory()
    token = token_factory(user=user)
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    # any authorised/unauthorised user can get all collections.
    resp = session.get(COLLECTION_BASE_URL)
    assert resp.status_code == 200


@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.django_db
def test_retrieve_collections_through_id(
        session_user_authorized, session_user_unauthorized,
        user_factory, superuser_factory, token_factory, is_authorized
):
    """
    Checks retrieve specific collection through:
    1) endpoint <id>
    2) url parameter <id>
    For authorised/unauthorised user.
    """
    # let's create some collections
    admin = superuser_factory()
    admin_token = token_factory(user=admin)
    admin_session = session_user_authorized(token=admin_token)
    [create_collection(admin_session) for _ in range(COLLECTIONS_COUNT)]
    # let's choice a specific collection as a testing data
    list_resp = admin_session.get(COLLECTION_BASE_URL)
    assert list_resp.status_code == 200
    list_json = list_resp.json()
    collection = choice(list_json)
    collection_id = collection['id']
    collection_header = collection['header']

    # define session state
    user = user_factory()
    token = token_factory(user=user)
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    # any authorised/unauthorised user can retrieve a specific collection via endpoint <id>
    resp_via_endpoint = session.get(urljoin(COLLECTION_BASE_URL, f'{collection_id}/'))
    assert resp_via_endpoint.status_code == 200
    # check getting the relevant collection
    retrieve_json = resp_via_endpoint.json()
    assert collection_header == retrieve_json['header']

    # any authorised/unauthorised user can retrieve a specific collection via parameter <id>
    payload = {'id': collection_id}
    resp_via_parameter = session.get(COLLECTION_BASE_URL, payload)
    assert resp_via_parameter.status_code == 200
    # check getting the relevant collection
    retrieve_json = resp_via_parameter.json()
    assert collection_header == retrieve_json[0]['header']


# POST

@mark.django_db
def test_create_collections(
        session_user_authorized, user_factory,
        superuser_factory, token_factory
):
    """
    Checks creating collections. For user/superuser.
    """
    # user can not create collections
    payload = get_payload()
    user = user_factory()
    user_token = token_factory(user=user)
    user_session = session_user_authorized(token=user_token)
    user_resp = user_session.post(COLLECTION_BASE_URL, payload)
    assert user_resp.status_code == 403

    # admin can
    admin = superuser_factory()
    admin_token = token_factory(user=admin)
    admin_session = session_user_authorized(token=admin_token)
    admin_resp = admin_session.post(COLLECTION_BASE_URL, payload)
    assert admin_resp.status_code == 201


# PUT, PATCH

@mark.django_db
def test_update_partial_update_collection(
        session_user_authorized, superuser_factory, token_factory
):
    """
    Checks update/partial_update of collection. For superuser.
    """
    # let's create a collection
    admin_session = session_user_authorized(
        token=token_factory(
            user=superuser_factory()
        )
    )
    initial_payload = get_payload()
    create_resp = admin_session.post(COLLECTION_BASE_URL, initial_payload)
    assert create_resp.status_code == 201
    create_json = create_resp.json()
    coll_id = create_json['id']
    coll_initial_header = create_json['header']

    # attempt of update/partial_update of collection
    for method in (admin_session.put, admin_session.patch):
        new_payload = get_payload()
        change_url = urljoin(COLLECTION_BASE_URL, '{}/'.format(coll_id))
        change_resp = method(change_url, new_payload)
        assert change_resp.status_code == 200
        change_json = change_resp.json()
        coll_modified_header = change_json['header']
        assert coll_initial_header != coll_modified_header


# DELETE

@mark.django_db
def test_destroy_collection(
        session_user_authorized, user_factory, superuser_factory, token_factory
):
    """
    Checks deleting of collection. For user/superuser.
    """
    user_session = session_user_authorized(
        token=token_factory(
            user=user_factory()
        )
    )
    admin_session = session_user_authorized(
        token=token_factory(
            user=superuser_factory()
        )
    )
    # let's create a collection
    create_resp = admin_session.post(COLLECTION_BASE_URL, get_payload())
    assert create_resp.status_code == 201
    collection_id = create_resp.json()['id']
    url = urljoin(COLLECTION_BASE_URL, '{}/'.format(collection_id))

    # user can not delete collection
    user_delete_resp = user_session.delete(url)
    assert user_delete_resp.status_code == 403
    # admin can
    admin_delete_resp = admin_session.delete(url)
    assert admin_delete_resp.status_code == 204
