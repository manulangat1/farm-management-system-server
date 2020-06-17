from rest_framework import serializers

from .models import Cow,Parturation,Feed,Treatment

class CowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cow
        fields = (
            'id',
            'name',
            'dob',
            'stage',
            'breed'
        )
class CowFulldetailSerializer(serializers.ModelSerializer):
    parturation = serializers.SerializerMethodField()
    class Meta:
        model = Cow
        fields = (
            'id',
            'name',
            'dob',
            'stage',
            'breed',
            'parturation'
        )
    def get_parturation(self,obj):
        return ParturationSerializer(obj.parturation.all(),many=True).data
class ParturationCreateSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Parturation
        fields = (
            'cow',
            'breed',
            'vet'
        )
class ParturationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Parturation
        fields = (
            'cow',
            'date_served',
            'expected_date',
            'breed',
            'vet'
        )

# class FeedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Feed
#         fields = (
#             'cow',
#             'amount',
#             'date'
#         )
