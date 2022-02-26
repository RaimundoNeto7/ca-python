from fastapi import FastAPI, HTTPException, status

from src.application.controllers.products_controller import (
    add_product_controller,
    get_products_controller,
)
from src.application.schemas.products import ProductsSchema

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Servidor discord"}


@app.get("/products")
def get_products():
    try:
        return get_products_controller()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.__traceback__
        )


@app.post("/products")
def post_products(product: ProductsSchema):
    try:
        return add_product_controller(**product.dict())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.__traceback__
        )
