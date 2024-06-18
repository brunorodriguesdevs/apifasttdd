from fastapi import FastAPI
from app.controllers import product_controller

app = FastAPI()

app.include_router(product_controller.router)
