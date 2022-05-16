import json

import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture()
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# Проверка получения 1го курса (retrieve-логика)
@pytest.mark.django_db
def test_retrieve_course(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.get(f'http://127.0.0.1:8000/courses/{course[0].id}/')
    data = response.json()

    assert response.status_code == 200
    assert data.get('id') == course[0].id
    assert data.get('name') == course[0].name


# Проверка фильтрации списка курсов по `id`
@pytest.mark.django_db
def test_filter_by_id(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get(f'http://127.0.0.1:8000/courses/')
    data = response.json()

    assert response.status_code == 200

    for element in data:
        id = {'id': element['id']}
        response = client.get(f'http://127.0.0.1:8000/courses/', id)
        assert response.status_code == 200

# Проверка фильтрации списка курсов по `name`
@pytest.mark.django_db
def test_filter_by_name(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get(f'http://127.0.0.1:8000/courses/')
    data = response.json()

    assert response.status_code == 200

    for element in data:
        name = {'name': element['name']}
        response = client.get(f'http://127.0.0.1:8000/courses/', name)
        assert response.status_code == 200


# Проверка получения списка курсов (list-логика)
@pytest.mark.django_db
def test_list_course(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get(f'http://127.0.0.1:8000/courses/')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


# Тест успешного создания курса
@pytest.mark.django_db
def test_making_course(client):
    courses_count = Course.objects.count()
    course = {"name": "Teanapping"}

    response = client.post('http://127.0.0.1:8000/courses/', data=course, format='json')

    assert response.status_code == 201
    assert Course.objects.count() == courses_count + 1


# Тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(_quantity=1)
    name = {'name': 'Andrew'}

    response = client.patch(f'http://127.0.0.1:8000/courses/{course[0].id}/', data=name)

    assert response.status_code == 200
    assert response.json().get('name') == name['name']


# Тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=1)
    courses_count = Course.objects.count()

    response = client.delete(f'http://127.0.0.1:8000/courses/{course[0].id}/')

    assert response.status_code == 204  # no content
    assert client.get(f'http://127.0.0.1:8000/courses/{course[0].id}/').status_code == 404  # not found
    assert Course.objects.count() == courses_count - 1


def test_example():
    assert True, "Just test example"
