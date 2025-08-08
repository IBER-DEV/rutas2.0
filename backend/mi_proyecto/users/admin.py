from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_driver', 'is_staff')
    list_filter = ('is_driver', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('phone', 'is_driver')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {'fields': ('phone', 'is_driver')}),
    )
