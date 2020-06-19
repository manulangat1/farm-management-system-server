import pytest
import datetime
from django.urls import reverse
from django.conf import settings
from pytest_postgresql import factories
postgresql_external = factories.postgresql('postgresql_nooproc')
@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'farm_management',
        'USER':'manulangat',
        'PASSWORD':'3050manu'
    }
@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.mark.django_db
def test_part_list(api_client,django_db_setup):
    url = reverse('parturation_list')
    res = api_client.get(url)
    assert res.status_code == 200
