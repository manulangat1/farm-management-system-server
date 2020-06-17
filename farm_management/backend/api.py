from rest_framework import generics
from rest_framework.response import Response

from .serializers import CowSerializer,CowFulldetailSerializer,ParturationCreateSerializer,ParturationSerializer
from .models import Cow,Parturation

import datetime

class CowAPI(generics.CreateAPIView):
    queryset = Cow.objects.all()
    serializer_class = CowSerializer
class CowListAPI(generics.ListAPIView):
    queryset = Cow.objects.all()
    serializer_class = CowFulldetailSerializer

class CowDetails(generics.RetrieveUpdateAPIView):
    queryset = Cow.objects.all()
    serializer_class = CowFulldetailSerializer

class ParturationAPI(generics.CreateAPIView):
    queryset = Parturation.objects.all()
    serializer_class = ParturationCreateSerializer
    def perform_create(self, serializer):
        d = datetime.timedelta(days=285)
        print(d)
        date_served = datetime.datetime.now()
        expected_date = date_served + d
        print(expected_date)
        return serializer.save(date_served=date_served,expected_date=expected_date)
class ParturationListAPI(generics.ListAPIView):
    queryset = Parturation.objects.all()
    serializer_class = ParturationSerializer
class ParturationDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parturation.objects.all()
    serializer_class = ParturationSerializer