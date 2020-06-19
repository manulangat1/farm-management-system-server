from django.urls import path
from .api import CowAPI,CowListAPI,CowDetails,ParturationAPI,ParturationListAPI,ParturationDetailAPI
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
schema_view = get_swagger_view(title='Farm Management Server API')


urlpatterns = [
    path('cow_create/',CowAPI.as_view(),name="cow_create"),
    path('cows/',CowListAPI.as_view(),name="cow_list"),
    path('cows/<pk>',CowDetails.as_view(),name="cow_details"),
    path('part/',ParturationAPI.as_view(),name="parturation_create"),
    path('part/list/',ParturationListAPI.as_view(),name="parturation_list"),

    path('part/<pk>/',ParturationDetailAPI.as_view(),name="parturation_detail"),
    path('openapi/', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('',schema_view)

]