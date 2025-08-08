from django.contrib import admin
from .models import BusLocation

@admin.register(BusLocation)
class BusLocationAdmin(admin.ModelAdmin):
    list_display = ('bus', 'lat', 'lng', 'speed', 'recorded_at')
    list_filter = ('bus', 'recorded_at')
    search_fields = ('bus__plate',)
    ordering = ('-recorded_at',)
    readonly_fields = ('recorded_at',)
    
    # Mostrar solo las últimas 100 ubicaciones por defecto
    list_per_page = 100
