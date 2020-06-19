import pytest
# from backed.models import Cow
from django.urls import reverse
import datetime
from django.conf import settings

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

@pytest.mark.django_db
def test_cow_list(api_client):
    url = reverse('cow_list')
    response = api_client.get(url)
    assert response.status_code == 200

# @pytest.mark.django_db
# def test_can_get_details(api_client):
#     now = datetime.datetime.now()
#     cow = Cow.objects.create(
#         now,
#         'manu',
#             'HEIFER',
#             'FRESIAN'
#     )
#     url = reverse('cow_list',kwargs={'pk': cow.pk})
#     res = api_client.get(url)
#     assert res.status_code == 200