import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def new_nota():
    return {"titulo": "Nota de prueba", "contenido": "Contenido de prueba"}

def test_create_nota(test_client: TestClient, new_nota):
    response = test_client.post("/notas/", json=new_nota)
    assert response.status_code == 201
    assert response.json()["titulo"] == new_nota["titulo"]

def test_get_nota(test_client: TestClient):
    response = test_client.get("/notas/1")
    assert response.status_code == 200
    assert "titulo" in response.json()

def test_update_nota(test_client: TestClient):
    update_data = {"titulo": "Nota actualizada"}
    response = test_client.put("/notas/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["titulo"] == update_data["titulo"]

def test_delete_nota(test_client: TestClient):
    response = test_client.delete("/notas/1")
    assert response.status_code == 204
