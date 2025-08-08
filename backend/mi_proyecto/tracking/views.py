from rest_framework import viewsets, permissions
from .models import BusLocation
from .serializers import BusLocationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class BusLocationViewSet(viewsets.ModelViewSet):
    queryset = BusLocation.objects.all()
    serializer_class = BusLocationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()
        # Broadcast location via channels
        channel_layer = get_channel_layer()
        group_name = f"bus_{instance.bus.id}"
        async_to_sync(channel_layer.group_send)(
            group_name,
            {
                "type": "bus.location",
                "lat": instance.lat,
                "lng": instance.lng,
                "speed": instance.speed,
                "bus_id": instance.bus.id,
                "recorded_at": instance.recorded_at.isoformat()
            }
        )
