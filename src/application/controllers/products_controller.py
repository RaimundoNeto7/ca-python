from src.domain.use_cases.add_product import AddProduct
from src.domain.use_cases.get_products import GetProducts
from src.infra.database.config import get_db
from src.infra.repository.products_repository_postgres import ProductsRepositoryPostgres


def get_products_controller():
    get_produtcs_use_case = GetProducts(ProductsRepositoryPostgres(get_db().__next__()))
    return get_produtcs_use_case.execute()


def add_product_controller(name, description, brand, price, quantity, is_active):
    add_product_use_case = AddProduct(
        ProductsRepositoryPostgres(get_db().__next__()),
        name,
        description,
        brand,
        price,
        quantity,
        is_active,
    )
    return add_product_use_case.execute()
