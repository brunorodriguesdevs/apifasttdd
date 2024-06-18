from typing import Optional
from app.models.product_model import ProductModel
from app.schemas.product_schema import ProductCreate, ProductUpdate

class ProductService:
    
    @staticmethod
    def create_product(product: ProductCreate):
        product_data = product.dict()
        return ProductModel.insert_one(product_data)

    @staticmethod
    def list_products(price_min: Optional[float], price_max: Optional[float]):
        query = {}
        if price_min is not None:
            query["price"] = {"$gt": price_min}
        if price_max is not None:
            query["price"] = {"$lt": price_max}
        return ProductModel.find(query)

    @staticmethod
    def get_product(product_id: str):
        return ProductModel.find_one({"_id": product_id})

    @staticmethod
    def update_product(product_id: str, product: ProductUpdate):
        update_data = product.dict(exclude_unset=True)
        return ProductModel.update_one({"_id": product_id}, {"$set": update_data})

    @staticmethod
    def delete_product(product_id: str):
        result = ProductModel.delete_one({"_id": product_id})
        return result.deleted_count > 0
