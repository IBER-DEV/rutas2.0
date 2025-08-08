from rest_framework import viewsets, permissions
from .models import Conductor, Bus, Ruta, Parada, Viaje
from .serializers import ConductorSerializer, BusSerializer, RutaSerializer, ParadaSerializer, ViajeSerializer

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer
    permission_classes = [permissions.IsAuthenticated]

class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    permission_classes = [permissions.IsAuthenticated]

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.prefetch_related('paradas').all()
    serializer_class = RutaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ParadaViewSet(viewsets.ModelViewSet):
    queryset = Parada.objects.all()
    serializer_class = ParadaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ViajeViewSet(viewsets.ModelViewSet):
    queryset = Viaje.objects.all()
    serializer_class = ViajeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # usuarios pueden ver solo sus viajes (admin lo ve todo)
        user = self.request.user
        if user.is_staff:
            return Viaje.objects.all()
        return Viaje.objects.filter(user=user)
