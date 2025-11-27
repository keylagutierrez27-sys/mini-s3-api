import requests
import json

BASE_URL = "http://localhost:5000/api"

def test_crear_bucket():
    """Prueba la creación de un bucket"""
    response = requests.post(
        f"{BASE_URL}/buckets",
        json={"name": "test-bucket"}
    )
    print(f"✓ Crear bucket: {response.status_code}")
    assert response.status_code == 201

def test_listar_buckets():
    """Prueba el listado de buckets"""
    response = requests.get(f"{BASE_URL}/buckets")
    print(f"✓ Listar buckets: {response.status_code}")
    assert response.status_code == 200

if __name__ == "__main__":
    print("Ejecutando pruebas...")
    test_crear_bucket()
    test_listar_buckets()
    print("¡Todas las pruebas pasaron!")