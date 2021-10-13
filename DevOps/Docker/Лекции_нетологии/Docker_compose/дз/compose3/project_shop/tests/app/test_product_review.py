from datetime import datetime
from random import randint, choice
from urllib.parse import urljoin

from django.urls import reverse
from faker import Faker
from pytest import mark, param

from app.models import ProductReview

REVIEW_BASE_URL = reverse('product-reviews-list')
REVIEW_BIG_QUANTITY = randint(500, 1000)
REVIEW_TEXT = Faker('ru_RU').text(randint(500, 1000))
REVIEW_GRADE = (randint(1, 6))


# GET

@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.django_db
def test_list_reviews(
        session_user_authorized, session_user_unauthorized,
        product_review_factory, token_factory,
        user_factory, is_authorized,
):
    """
    Checks getting all reviews for authorized/unauthorized user.
    """
    token = token_factory(user=user_factory())
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    product_review_factory(_quantity=REVIEW_BIG_QUANTITY, grade=REVIEW_GRADE)
    response = session.get(REVIEW_BASE_URL)
    assert response.status_code == 200
    assert len(response.json()) == REVIEW_BIG_QUANTITY


@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.django_db
def test_retrieve_review_through_id_endpoint(
        session_user_authorized, session_user_unauthorized,
        product_review_factory, token_factory,
        user_factory, is_authorized
):
    """
    Checks getting specific review through endpoint <id>.
    For authorized/unauthorized user.
    """
    token = token_factory(user=user_factory())
    product_review_factory(_quantity=REVIEW_BIG_QUANTITY, grade=REVIEW_GRADE)
    review_id = choice(ProductReview.objects.values_list('id', flat=True))
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    url = urljoin(REVIEW_BASE_URL, f'{review_id}/')
    response = session.get(url)
    assert response.status_code == 200


@mark.parametrize('id_or_creator', [
    param('id', id='Url parameter id'),
    param('creator', id='Url parameter creator'),
])
@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.django_db
def test_retrieve_review_through_id_or_creator_parameter(
        session_user_authorized, session_user_unauthorized,
        product_review_factory, token_factory,
        user_factory, id_or_creator, is_authorized
):
    """
    Checks getting specific review through url parameter <id> or <creator>.
    For authorized/unauthorized user.
    """
    token = token_factory(user=user_factory())
    product_review_factory(_quantity=REVIEW_BIG_QUANTITY, grade=REVIEW_GRADE)
    url_parameter = choice(ProductReview.objects.values_list(id_or_creator, flat=True))
    payload = {id_or_creator: url_parameter}
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    response = session.get(REVIEW_BASE_URL, payload)
    assert response.status_code == 200


@mark.parametrize('date_parameter', [
    param('created_at_before', id='Url parameter created_at_before'),
    param('created_at_after', id='Url parameter created_at_after'),
])
@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.django_db
def test_retrieve_review_through_date_parameter(
        session_user_authorized, session_user_unauthorized,
        product_review_factory, token_factory,
        user_factory, date_parameter, is_authorized
):
    """
    Checks getting specific review through url parameter <created_at_before>
    or <created_at_after>. For authorized/unauthorized user.
    """
    token = token_factory(user=user_factory())
    product_review_factory(_quantity=REVIEW_BIG_QUANTITY, grade=REVIEW_GRADE)
    payload = {date_parameter: datetime.now().date()}
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    response = session.get(REVIEW_BASE_URL, payload)
    assert response.status_code == 200


@mark.parametrize('is_authorized', [
    param(True, id='User authorized'),
    param(False, id='User not authorized'),
])
@mark.django_db
def test_retrieve_review_through_product_parameter(
        session_user_authorized, session_user_unauthorized,
        product_review_factory, token_factory,
        user_factory, is_authorized,
):
    """
    Checks getting specific review through url parameter <product>.
    For authorized/unauthorized user.
    """
    token = token_factory(user=user_factory())
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    product_review_factory(_quantity=REVIEW_BIG_QUANTITY, grade=REVIEW_GRADE)
    common_response = session.get(REVIEW_BASE_URL)

    product = choice(common_response.json())['product']
    payload = {'product': product}
    detail_response = session.get(REVIEW_BASE_URL, payload)
    assert detail_response.status_code == 200


# POST

@mark.parametrize('is_authorized, expected_status_code', [
    param(True, 201, id='User authorized'),
    param(False, 401, id='User not authorized'),
])
@mark.django_db
def test_create_review(
        session_user_authorized, session_user_unauthorized,
        product_factory, token_factory,
        user_factory, is_authorized, expected_status_code,
):
    """
    Checks possibility/impossibility of creating review
    for authorized/unauthorized user.
    """
    product = product_factory()
    user = user_factory()
    token = token_factory(user=user)
    session = session_user_authorized(token=token) \
        if is_authorized else session_user_unauthorized
    payload = {
        "text": REVIEW_TEXT,
        "grade": REVIEW_GRADE,
        "product": product.pk,
        "creator": user.pk
    }
    response = session.post(REVIEW_BASE_URL, payload)
    assert response.status_code == expected_status_code


@mark.django_db
def test_create_repeated_review(
        session_user_authorized, user_factory,
        product_factory, token_factory,
):
    """
    Checks impossibility of creating repeated review for
    the same product for one user.
    """
    product = product_factory()
    user = user_factory()
    token = token_factory(user=user)
    session = session_user_authorized(token=token)
    payload = {
        "text": REVIEW_TEXT,
        "grade": REVIEW_GRADE,
        "product": product.pk,
        "creator": user.pk
    }
    first_response = session.post(REVIEW_BASE_URL, payload)
    assert first_response.status_code == 201

    repeated_response = session.post(REVIEW_BASE_URL, payload)
    assert repeated_response.status_code == 400


# PUT, PATCH, DELETE

@mark.django_db
def test_update_partial_update_destroy_review(
        session_user_authorized, user_factory,
        product_factory, token_factory
):
    """
    Checks possibility/impossibility of update/partial_update/destroy review.
    For creator/not creator.
    """
    product = product_factory()
    creator = user_factory()
    token = token_factory(user=creator)
    creator_session = session_user_authorized(token=token)
    create_payload = {
        "text": REVIEW_TEXT,
        "grade": REVIEW_GRADE,
        "product": product.pk,
        "creator": creator.pk
    }
    create_response = creator_session.post(REVIEW_BASE_URL, create_payload)
    assert create_response.status_code == 201

    review_id = create_response.json()['id']
    update_payload = {
        "id": review_id,
        "text": REVIEW_TEXT.upper(),
        "grade": REVIEW_GRADE,
        "product": product.pk,
        "creator": creator.pk
    }
    url_for_change = urljoin(REVIEW_BASE_URL, f'{review_id}/')
    creator_put_response = creator_session.put(url_for_change, update_payload)
    assert creator_put_response.status_code == 200
    creator_patch_response = creator_session.patch(url_for_change, update_payload)
    assert creator_patch_response.status_code == 200

    not_creator = user_factory()
    not_creator_token = token_factory(user=not_creator)
    not_creator_session = session_user_authorized(token=not_creator_token)
    not_creator_payload = {
        "id": review_id,
        "text": REVIEW_TEXT.lower(),
        "grade": REVIEW_GRADE,
        "product": product.pk,
        "creator": not_creator.pk
    }
    not_creator_put_response = not_creator_session.put(url_for_change, not_creator_payload)
    assert not_creator_put_response.status_code == 403
    not_creator_patch_response = not_creator_session.patch(url_for_change, not_creator_payload)
    assert not_creator_patch_response.status_code == 403

    not_creator_delete_response = not_creator_session.delete(url_for_change)
    assert not_creator_delete_response.status_code == 403

    creator_delete_response = creator_session.delete(url_for_change)
    assert creator_delete_response.status_code == 204
