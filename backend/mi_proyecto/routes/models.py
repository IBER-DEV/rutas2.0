from django.db import models
from django.conf import settings

class Conductor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=50)

    def __str__(self): return f"{self.user.get_full_name()}"

class Bus(models.Model):
    plate = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField(default=20)
    status = models.CharField(max_length=20, choices=[('active','Active'),('maintenance','Maintenance')], default='active')
    driver = models.ForeignKey(Conductor, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self): return self.plate

class Ruta(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    bus = models.ForeignKey(Bus, null=True, blank=True, on_delete=models.SET_NULL)
    estimated_duration_min = models.IntegerField(default=60)

    def __str__(self): return self.name

class Parada(models.Model):
    ruta = models.ForeignKey(Ruta, related_name="paradas", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    order = models.IntegerField()
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        ordering = ['order']

    def __str__(self): return f"{self.ruta.name} - {self.order} - {self.name}"

class Viaje(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    origin = models.ForeignKey(Parada, related_name='viajes_origen', null=True, blank=True, on_delete=models.SET_NULL)
    destination = models.ForeignKey(Parada, related_name='viajes_destino', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=[('ongoing','Ongoing'),('completed','Completed'),('cancelled','Cancelled')], default='ongoing')

    def __str__(self): return f"{self.user} - {self.ruta} - {self.start_time}"
