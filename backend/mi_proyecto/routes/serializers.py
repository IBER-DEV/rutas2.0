from rest_framework import serializers
from .models import Conductor, Bus, Ruta, Parada, Viaje
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email","phone","is_driver"]

class ConductorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Conductor
        fields = "__all__"

class BusSerializer(serializers.ModelSerializer):
    driver = ConductorSerializer(read_only=True)
    class Meta:
        model = Bus
        fields = "__all__"

class ParadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parada
        fields = "__all__"

class RutaSerializer(serializers.ModelSerializer):
    paradas = ParadaSerializer(many=True, read_only=True)
    bus = BusSerializer(read_only=True)
    class Meta:
        model = Ruta
        fields = "__all__"

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = "__all__"
