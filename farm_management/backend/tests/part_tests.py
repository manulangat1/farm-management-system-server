import pytest
import datetime
from django.urls import reverse
@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.mark.django_db
def test_part_list(api_client):
    url = reverse('parturation_list')
    res = api_client.get(url)
    assert res.status_code == 200
