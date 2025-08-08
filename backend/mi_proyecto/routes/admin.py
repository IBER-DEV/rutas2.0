from django.contrib import admin
from .models import Conductor, Bus, Ruta, Parada, Viaje

@admin.register(Conductor)
class ConductorAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'license_number')
    list_filter = ('user__is_active',)

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('plate', 'capacity', 'status', 'driver')
    list_filter = ('status', 'capacity')
    search_fields = ('plate', 'driver__user__username')
    ordering = ('plate',)

@admin.register(Ruta)
class RutaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'bus', 'estimated_duration_min')
    list_filter = ('estimated_duration_min',)
    search_fields = ('code', 'name', 'description')
    ordering = ('code',)

@admin.register(Parada)
class ParadaAdmin(admin.ModelAdmin):
    list_display = ('name', 'ruta', 'order', 'lat', 'lng')
    list_filter = ('ruta',)
    search_fields = ('name', 'ruta__name')
    ordering = ('ruta', 'order')

@admin.register(Viaje)
class ViajeAdmin(admin.ModelAdmin):
    list_display = ('user', 'ruta', 'start_time', 'end_time', 'status')
    list_filter = ('status', 'start_time', 'ruta')
    search_fields = ('user__username', 'ruta__name')
    ordering = ('-start_time',)
    readonly_fields = ('start_time',)
