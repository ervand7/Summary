from random import randint
from urllib.parse import urljoin

from django.conf import settings
from django.urls import reverse
from mimesis import Person
from mimesis.enums import Gender
from pytest import mark, param

from students.models import Course

COURSE_BASE_API_URL = reverse('courses-list')
COURSE_NAME = Person('it').surname(gender=Gender.FEMALE)
COURSE_BIG_QUANTITY = randint(2, 1000)


@mark.parametrize('course_quantity', [
    param(1, id='First course'),
    param(COURSE_BIG_QUANTITY, id='Many courses'),
])
@mark.django_db
def test_getting_course(api_client, course_factory, course_quantity):
    failed_msd = 'Not valid courses were detected: \n{0}'
    course_factory(_quantity=course_quantity)  # _quantity - зарезервированный параметр
    # обязательно дописываем к названию урла <-list>, иначе не заработает
    response = api_client.get(COURSE_BASE_API_URL)

    assert response.status_code == 200
    courses = response.data
    courses_count = len(courses)
    assert courses_count == course_quantity
    failed_courses_list = [
        course for course in courses if not course['id'] or not course['name']
    ]
    assert not failed_courses_list, failed_msd.format(failed_courses_list)


@mark.django_db
def test_course_filter_id(api_client, course_factory):
    course_factory(_quantity=COURSE_BIG_QUANTITY)
    all_courses_response = api_client.get(COURSE_BASE_API_URL)
    assert all_courses_response.status_code == 200

    random_index = randint(0, COURSE_BIG_QUANTITY - 1)
    all_courses = all_courses_response.data
    random_course = all_courses[random_index]
    _id = random_course['id']
    filter_id_payload = {'id': _id}

    filter_id_response = api_client.get(COURSE_BASE_API_URL, filter_id_payload)
    assert filter_id_response.status_code == 200
    assert len(filter_id_response.data) == 1
    filtered_course = filter_id_response.data[0]
    assert filtered_course['id'] == _id


@mark.django_db
def test_course_filter_name(api_client, course_factory):
    Course.objects.create(name=COURSE_NAME)
    course_payload = {'name': COURSE_NAME}
    response = api_client.get(COURSE_BASE_API_URL, course_payload)

    assert response.status_code == 200
    courses = response.data
    expected_course_name_from_api = courses[0]['name']
    assert expected_course_name_from_api == COURSE_NAME


@mark.django_db
def test_course_create(api_client, course_factory):
    course_create_payload = {'name': COURSE_NAME}
    response_create = api_client.post(
        COURSE_BASE_API_URL, course_create_payload
    )
    assert response_create.status_code == 201
    response_get = api_client.get(COURSE_BASE_API_URL)
    assert response_get.status_code == 200
    course = response_get.data[0]
    assert course


@mark.django_db
def test_course_update(api_client, course_factory):
    course_factory(_quantity=1)
    get_response = api_client.get(COURSE_BASE_API_URL)
    assert get_response.status_code == 200

    course_before = get_response.data[0]
    course_name_before = course_before['name']
    course_id = course_before['id']
    new_course_name = COURSE_NAME
    update_payload = {'name': new_course_name}
    update_response = api_client.patch(
        urljoin(COURSE_BASE_API_URL, f'{course_id}/'), update_payload
    )

    assert update_response.status_code == 200
    course_after = update_response.data
    course_name_after = course_after['name']
    assert course_name_before != course_name_after


@mark.django_db
def test_course_delete(api_client, course_factory):
    courses_count_before = COURSE_BIG_QUANTITY
    course_factory(_quantity=courses_count_before)
    get_response_before = api_client.get(COURSE_BASE_API_URL)
    assert get_response_before.status_code == 200

    random_index = randint(0, courses_count_before - 1)
    courses_before_deleting = get_response_before.data
    course_for_delete = courses_before_deleting[random_index]
    _id = course_for_delete['id']
    delete_response = api_client.delete(urljoin(COURSE_BASE_API_URL, f'{_id}/'))
    assert delete_response.status_code == 204

    get_response_after = api_client.get(COURSE_BASE_API_URL)
    assert get_response_after.status_code == 200
    courses_count_after = len(get_response_after.data)
    assert courses_count_before - 1 == courses_count_after
    courses_after_deleting = get_response_after.data
    assert _id not in [course['id'] for course in courses_after_deleting]


@mark.parametrize('students_count, expected_status', [
    param(settings.MAX_STUDENTS_PER_COURSE, 201, id='Maximum allowable value'),
    param(settings.MAX_STUDENTS_PER_COURSE + 1, 400, id='Beyond value'),
])
@mark.django_db
def test_course_validation_student_max_count(
    api_client, student_factory, students_count, expected_status
):
    students = student_factory(_quantity=students_count)
    students_ids_list = list()
    [students_ids_list.append(s.id) for s in students]

    payload = {'name': COURSE_NAME, 'students': students_ids_list}
    response = api_client.post(COURSE_BASE_API_URL, payload)
    actual_status = response.status_code
    assert expected_status == actual_status

