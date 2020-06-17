import pytest


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'farm_management',
        'USER':'manulangat',
        'PASSWORD':'3050manu'
    }