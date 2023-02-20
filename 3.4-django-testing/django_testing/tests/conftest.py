from model_bakery import baker
from rest_framework.test import APIClient
import pytest

from django_testing import local_settings


@pytest.fixture
def client():
    return APIClient


@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make('Course', **kwargs)
    return factory


@pytest.fixture
def course_data():
    return {'name': 'Курс по Python'}


@pytest.fixture
def max_students():
    return local_settings.MAX_STUDENTS_PER_COURSE
