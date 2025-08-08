from rest_framework import serializers
from .models import BusLocation

class BusLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusLocation
        fields = "__all__"
