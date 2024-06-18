from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={"name": "Product1", "price": 1000})
    assert response.status_code == 201
    assert response.json()["name"] == "Product1"

def test_list_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_product():
    response = client.post("/products/", json={"name": "Product2", "price": 1500})
    product_id = response.json()["_id"]
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Product2"

def test_update_product():
    response = client.post("/products/", json={"name": "Product3", "price": 2000})
    product_id = response.json()["_id"]
    response = client.patch(f"/products/{product_id}", json={"name": "Updated Product", "price": 2500})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"

def test_delete_product():
    response = client.post("/products/", json={"name": "Product4", "price": 3000})
    product_id = response.json()["_id"]
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Product deleted successfully"
