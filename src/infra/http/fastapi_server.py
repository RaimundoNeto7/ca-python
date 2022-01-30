from fastapi import FastAPI

from src.application.controllers.products_controller import get_products_controller

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Servidor discord"}


@app.get("/products")
def get_products():
    return get_products_controller()
