import pytest
from pydantic import ValidationError
from app.schemas.product_schema import ProductCreate

def test_product_create_schema():
    product = ProductCreate(name="Product1", price=1000)
    assert product.name == "Product1"
    assert product.price == 1000

def test_product_create_schema_invalid():
    with pytest.raises(ValidationError):
        ProductCreate(name="Product1", price="invalid")
