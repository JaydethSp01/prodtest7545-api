import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def new_category():
    return {
        "name": "Test Category"
    }

def test_create_category(test_client: TestClient, new_category):
    response = test_client.post("/categorias/", json=new_category)
    assert response.status_code == 201
    assert response.json()["name"] == new_category["name"]

def test_list_notes_by_category(test_client: TestClient, new_category, new_note):
    category_response = test_client.post("/categorias/", json=new_category)
    category_id = category_response.json()["id"]
    new_note["category_id"] = category_id
    test_client.post("/notas/", json=new_note)
    response = test_client.get(f"/categorias/{category_id}/notas")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["category_id"] == category_id
