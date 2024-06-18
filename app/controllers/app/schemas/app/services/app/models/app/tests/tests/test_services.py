import pytest
from app.services.product_service import ProductService
from app.schemas.product_schema import ProductCreate, ProductUpdate

@pytest.fixture
def new_product():
    return ProductCreate(name="Product1", price=1000)

def test_create_product(new_product):
    result = ProductService.create_product(new_product)
    assert result is not None

def test_list_products():
    products = ProductService.list_products(price_min=500, price_max=1500)
    assert len(products) > 0

def test_update_product(new_product):
    product_id = ProductService.create_product(new_product)["_id"]
    updated_product = ProductUpdate(name="Updated Product", price=1200)
    result = ProductService.update_product(product_id, updated_product)
    assert result is not None
    assert result["name"] == "Updated Product"
