# hotels/serializers.py
from rest_framework import serializers
from .models import Hotel
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class HotelSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'location', 'rating']
        geo_field = 'location'
