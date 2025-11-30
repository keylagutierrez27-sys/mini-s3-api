"""
Pruebas Automatizadas para Mini-S3 API
"""
import requests
import sys

BASE_URL = "http://localhost:5000/api"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_success(message):
    print(f"{Colors.GREEN}✓ {message}{Colors.RESET}")

def print_error(message):
    print(f"{Colors.RED}✗ {message}{Colors.RESET}")

def print_info(message):
    print(f"{Colors.BLUE}ℹ {message}{Colors.RESET}")

def print_header(message):
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'=' * 70}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{message}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 70}{Colors.RESET}\n")

def test_health_check():
    print_info("Ejecutando: Health Check...")
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert data["status"] == "healthy"
        print_success(f"Health Check: {response.status_code} OK")
        return True
    except Exception as e:
        print_error(f"Fallo: {e}")
        return False

def test_crear_bucket():
    print_info("Ejecutando: Crear Bucket...")
    try:
        response = requests.post(f"{BASE_URL}/buckets", json={"name": "test-bucket"}, timeout=5)
        assert response.status_code == 201
        data = response.json()
        assert "bucket" in data
        print_success(f"Crear Bucket: {response.status_code} Created")
        return True
    except Exception as e:
        print_error(f"Fallo: {e}")
        return False

def test_listar_buckets():
    print_info("Ejecutando: Listar Buckets...")
    try:
        response = requests.get(f"{BASE_URL}/buckets", timeout=5)
        assert response.status_code == 200
        data = response.json()
        assert "buckets" in data
        print_success(f"Listar Buckets: {response.status_code} OK")
        print_info(f"  Total: {data['count']} buckets")
        return True
    except Exception as e:
        print_error(f"Fallo: {e}")
        return False

def test_subir_objeto():
    print_info("Ejecutando: Subir Objeto...")
    try:
        response = requests.post(
            f"{BASE_URL}/buckets/test-bucket/objects",
            json={
                "key": "test/archivo.txt",
                "content": "RXN0ZSBlcyB1biBhcmNoaXZvIGRlIHBydWViYQ==",
                "contentType": "text/plain",
                "metadata": {"author": "Test"}
            },
            timeout=5
        )
        assert response.status_code == 201
        print_success(f"Subir Objeto: {response.status_code} Created")
        return True
    except Exception as e:
        print_error(f"Fallo: {e}")
        return False

def test_listar_objetos():
    print_info("Ejecutando: Listar Objetos...")
    try:
        response = requests.get(f"{BASE_URL}/buckets/test-bucket/objects", timeout=5)
        assert response.status_code == 200
        data = response.json()
        assert "objects" in data
        print_success(f"Listar Objetos: {response.status_code} OK")
        print_info(f"  Total: {data['count']} objetos")
        return True
    except Exception as e:
        print_error(f"Fallo: {e}")
        return False

def test_eliminar_objeto():
    print_info("Ejecutando: Eliminar Objeto...")
    try:
        response = requests.delete(f"{BASE_URL}/buckets/test-bucket/objects/test/archivo.txt", timeout=5)
        assert response.status_code == 200
        print_success(f"Eliminar Objeto: {response.status_code} OK")
        return True
    except Exception as e:
        print_error(f"Fallo: {e}")
        return False

def test_eliminar_bucket():
    print_info("Ejecutando: Eliminar Bucket...")
    try:
        response = requests.delete(f"{BASE_URL}/buckets/test-bucket", timeout=5)
        assert response.status_code == 200
        print_success(f"Eliminar Bucket: {response.status_code} OK")
        return True
    except Exception as e:
        print_error(f"Fallo: {e}")
        return False

def limpiar_datos():
    try:
        requests.delete(f"{BASE_URL}/buckets/test-bucket/objects/test/archivo.txt", timeout=5)
    except:
        pass
    try:
        requests.delete(f"{BASE_URL}/buckets/test-bucket", timeout=5)
    except:
        pass

def main():
    print_header("MINI-S3 API - PRUEBAS AUTOMATIZADAS")
    print(f"URL Base: {BASE_URL}\n")
    
    limpiar_datos()
    
    tests = [
        ("Health Check", test_health_check),
        ("Crear Bucket", test_crear_bucket),
        ("Listar Buckets", test_listar_buckets),
        ("Subir Objeto", test_subir_objeto),
        ("Listar Objetos", test_listar_objetos),
        ("Eliminar Objeto", test_eliminar_objeto),
        ("Eliminar Bucket", test_eliminar_bucket),
    ]
    
    resultados = []
    
    for nombre, test_func in tests:
        print(f"\n{Colors.BOLD}Prueba: {nombre}{Colors.RESET}")
        print("-" * 70)
        resultado = test_func()
        resultados.append((nombre, resultado))
    
    print_header("RESUMEN DE PRUEBAS")
    
    exitosas = sum(1 for _, r in resultados if r)
    fallidas = len(resultados) - exitosas
    
    print(f"Total: {len(resultados)}")
    print(f"{Colors.GREEN}Exitosas: {exitosas}{Colors.RESET}")
    print(f"{Colors.RED}Fallidas: {fallidas}{Colors.RESET}\n")
    
    for nombre, resultado in resultados:
        estado = f"{Colors.GREEN}✓ PASÓ{Colors.RESET}" if resultado else f"{Colors.RED}✗ FALLÓ{Colors.RESET}"
        print(f"  {estado} - {nombre}")
    
    if fallidas == 0:
        print_header(f"{Colors.GREEN}¡TODAS LAS PRUEBAS PASARON!{Colors.RESET}")
        sys.exit(0)
    else:
        print_header(f"{Colors.RED}ALGUNAS PRUEBAS FALLARON{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
