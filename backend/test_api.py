#!/usr/bin/env python3
"""
Script para probar la API del backend
"""
import requests
import json

# Configuración
BASE_URL = "http://localhost:8000"
API_URL = f"{BASE_URL}/api/rutas/public/"

def test_public_endpoint():
    """Prueba el endpoint público de rutas"""
    try:
        print(f"Probando endpoint: {API_URL}")
        response = requests.get(API_URL)
        
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Respuesta exitosa:")
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(f"Error en la respuesta:")
            print(response.text)
            
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar al servidor. Asegúrate de que Django esté ejecutándose.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def test_authenticated_endpoint():
    """Prueba el endpoint autenticado de rutas"""
    try:
        auth_url = f"{BASE_URL}/api/rutas/"
        print(f"\nProbando endpoint autenticado: {auth_url}")
        
        response = requests.get(auth_url)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 401:
            print("✅ Correcto: El endpoint requiere autenticación")
        else:
            print(f"⚠️  Inesperado: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("=== Prueba de la API del Backend ===\n")
    
    test_public_endpoint()
    test_authenticated_endpoint()
    
    print("\n=== Fin de las pruebas ===")
