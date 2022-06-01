import os

from fastapi import FastAPI, HTTPException, status

from src.application.controllers.products_controller import (
    ProductsController,
    add_product_controller,
    get_products_controller,
)
from src.application.schemas.products import ProductsSchema
from src.infra.database.config import get_db, init_db
from src.infra.repository.products_repository_postgres import ProductsRepositoryPostgres

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    init_db()


@app.get("/")
def read_root():
    return {"status": "Running", "env": os.getenv("ENV")}


@app.get("/products")
def get_products():
    try:
        with get_db() as session:
            repository = ProductsRepositoryPostgres(session=session)
            products_controller = ProductsController(repository=repository)
            return products_controller.get_products_controller()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.__traceback__
        )


@app.post("/products")
def post_products(product: ProductsSchema):
    try:
        with get_db() as session:
            repository = ProductsRepositoryPostgres(session=session)
            products_controller = ProductsController(repository=repository)
        return products_controller.add_product_controller(**product.dict())
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.__traceback__
        )
