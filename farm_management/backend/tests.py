from django.test import TestCase

# Create your tests here.
import pytest
# from backed.models import Cow
from django.urls import reverse
import datetime

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
@pytest.mark.django_db
def test_cow_create(api_client):
    now = datetime.datetime.now()
    data = {
        'dob':now,
        'name':'manu',
        'stage':'HEIFER',
        'breed':'FRESIAN'
    }
    url = reverse('cow_create')
    response = api_client.post(url,data)
    assert response.status_code == 201