import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def new_categoria():
    return {"nombre": "Categoria de prueba"}

def test_create_categoria(test_client: TestClient, new_categoria):
    response = test_client.post("/categorias/", json=new_categoria)
    assert response.status_code == 201
    assert response.json()["nombre"] == new_categoria["nombre"]

def test_get_categoria(test_client: TestClient):
    response = test_client.get("/categorias/1")
    assert response.status_code == 200
    assert "nombre" in response.json()

def test_update_categoria(test_client: TestClient):
    update_data = {"nombre": "Categoria actualizada"}
    response = test_client.put("/categorias/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["nombre"] == update_data["nombre"]

def test_delete_categoria(test_client: TestClient):
    response = test_client.delete("/categorias/1")
    assert response.status_code == 204
