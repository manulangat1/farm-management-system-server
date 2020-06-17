from django.urls import path
from .api import CowAPI,CowListAPI,CowDetails,ParturationAPI
urlpatterns = [
    path('',CowAPI.as_view(),name="cow_create"),
    path('cows/',CowListAPI.as_view(),name="cow_list"),
    path('cows/<pk>',CowDetails.as_view(),name="cow_details"),
    path('part/',ParturationAPI.as_view(),name="parturation_create"),
]