""" import sys
sys.path.append('src')
from src.app import app

def test_taxis():
    # Crear el cliente de pruebas
    client = app.test_client()

    # Hacer una solicitud GET a /taxis
    response = client.get("/taxis")
    
    # Verificar que el código de estado es 200
    assert response.status_code == 200, "El código de estado debe ser 200"
    
    # Verificar que el estado es 'OK'
    assert response.reason == "OK", "El estado de la respuesta debe ser 'OK'" """