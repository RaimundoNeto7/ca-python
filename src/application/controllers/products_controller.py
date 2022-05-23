from src.domain.use_cases.add_product import AddProduct
from src.domain.use_cases.get_products import GetProducts
from src.infra.database.config import get_db
from src.infra.repository.products_repository_postgres import ProductsRepositoryPostgres


def get_products_controller():
    with get_db() as session:
        get_produtcs_use_case = GetProducts(ProductsRepositoryPostgres(session))
        return get_produtcs_use_case.execute()


def add_product_controller(name, description, brand, price, quantity, is_active):
    with get_db() as session:
        add_product_use_case = AddProduct(
            ProductsRepositoryPostgres(session),
            name,
            description,
            brand,
            price,
            quantity,
            is_active,
        )
        return add_product_use_case.execute()
