from django.db import models
from routes.models import Bus
from django.utils import timezone

class BusLocation(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name='locations')
    lat = models.FloatField()
    lng = models.FloatField()
    speed = models.FloatField(null=True, blank=True)
    recorded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-recorded_at']
