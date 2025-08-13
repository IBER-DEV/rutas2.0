#!/usr/bin/env python3
"""
Script para crear un usuario de prueba en Django
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.mi_proyecto.settings')
django.setup()

from django.contrib.auth import get_user_model
from users.models import User

User = get_user_model()

def create_test_user():
    """Crea un usuario de prueba"""
    try:
        # Verificar si el usuario ya existe
        if User.objects.filter(username='admin').exists():
            print("✅ Usuario 'admin' ya existe")
            user = User.objects.get(username='admin')
            # Cambiar la contraseña a 'admin'
            user.set_password('admin')
            user.save()
            print("✅ Contraseña actualizada a 'admin'")
        else:
            # Crear nuevo usuario
            user = User.objects.create_user(
                username='admin',
                email='admin@example.com',
                password='admin',
                is_staff=True,
                is_superuser=True
            )
            print("✅ Usuario 'admin' creado exitosamente")
        
        print(f"Usuario: {user.username}")
        print(f"Email: {user.email}")
        print(f"Es staff: {user.is_staff}")
        print(f"Es superusuario: {user.is_superuser}")
        
    except Exception as e:
        print(f"❌ Error al crear usuario: {e}")

if __name__ == "__main__":
    print("=== Creando Usuario de Prueba ===\n")
    create_test_user()
    print("\n=== Fin ===")
