import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def new_usuario():
    return {"username": "usuario_prueba", "email": "prueba@example.com", "password": "password123"}

def test_create_usuario(test_client: TestClient, new_usuario):
    response = test_client.post("/usuarios/", json=new_usuario)
    assert response.status_code == 201
    assert response.json()["username"] == new_usuario["username"]

def test_get_usuario(test_client: TestClient):
    response = test_client.get("/usuarios/1")
    assert response.status_code == 200
    assert "username" in response.json()

def test_update_usuario(test_client: TestClient):
    update_data = {"username": "usuario_actualizado"}
    response = test_client.put("/usuarios/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["username"] == update_data["username"]

def test_delete_usuario(test_client: TestClient):
    response = test_client.delete("/usuarios/1")
    assert response.status_code == 204
