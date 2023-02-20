import pytest as pytest
from django.urls import reverse
from students.serializers import CourseSerializer


@pytest.mark.django_db
def test_detail_course(client, course_factory):
    course_factory(_quantity=10)
    url = reverse("courses-detail", kwargs={'pk': 2})
    response = client().get(url)

    assert response.status_code == 200
    assert response.data['id'] == 2


@pytest.mark.django_db
def test_list_course(client, course_factory):
    course_factory(_quantity=10)
    url = reverse("courses-list")
    response = client().get(url)

    assert response.status_code == 200
    assert len(response.data) == 10


@pytest.mark.django_db
def test_id_filter_course(client, course_factory):
    course_factory(_quantity=10)
    url = reverse("courses-list")
    response = client().get(url, {'id': 2})

    assert response.status_code == 200


@pytest.mark.django_db
def test_name_filter_course(client, course_factory):
    dammy_data = course_factory(_quantity=10)
    dammy_data_name = dammy_data[0].name
    url = reverse("courses-list")
    response = client().get(url, {'name': dammy_data_name})

    assert response.status_code == 200
    assert response.data[0]['name'] == dammy_data_name


@pytest.mark.django_db
def test_create_course(client, course_data):
    url = reverse("courses-list")
    response = client().post(url, course_data)

    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory, course_data):
    dammy_data = course_factory(_quantity=10)
    dammy_data_id = dammy_data[0].id
    url = reverse("courses-detail", kwargs={'pk': dammy_data_id})
    response = client().patch(url, course_data)

    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    dammy_data = course_factory(_quantity=10)
    dammy_data_id = dammy_data[0].id
    url = reverse("courses-detail", kwargs={'pk': dammy_data_id})
    response = client().delete(url)

    assert response.status_code == 204


@pytest.mark.parametrize(
    ['students', 'status'],
    (
        (5, 201),
        (21, 201),
        (25, 400)
    )
)


@pytest.mark.django_db
def test_max_students_course(students, status):
    students = [i for i in range(1, students)]
    validate_resp = CourseSerializer.validate_students(self=None, students=students)
    assert validate_resp == status