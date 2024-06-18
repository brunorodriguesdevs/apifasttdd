from fastapi import APIRouter, HTTPException
from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.services.product_service import ProductService
from app.database import get_db
from pymongo.errors import PyMongoError

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=dict)
async def create_product(product: ProductCreate):
    try:
        result = ProductService.create_product(product)
        return result
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model=list)
async def list_products(price_min: float = None, price_max: float = None):
    return ProductService.list_products(price_min, price_max)

@router.get("/{product_id}", response_model=dict)
async def get_product(product_id: str):
    product = ProductService.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.patch("/{product_id}", response_model=dict)
async def update_product(product_id: str, product: ProductUpdate):
    try:
        updated_product = ProductService.update_product(product_id, product)
        if not updated_product:
            raise HTTPException(status_code=404, detail="Product not found")
        return updated_product
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{product_id}", response_model=dict)
async def delete_product(product_id: str):
    if not ProductService.delete_product(product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
