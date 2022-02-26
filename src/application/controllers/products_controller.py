from src.domain.use_cases.add_product import AddProduct
from src.domain.use_cases.get_products import GetProducts
from src.infra.repository.memory_repository import MemoryProductsRepository

mem_repository = MemoryProductsRepository()


def get_products_controller():
    # mem_repository = MemoryProductsRepository()
    get_produtcs_use_case = GetProducts(mem_repository)
    return get_produtcs_use_case.execute()


def add_product_controller(name, description, brand, price, quantity, is_active):
    # mem_repository = MemoryProductsRepository()
    add_product_use_case = AddProduct(
        mem_repository, name, description, brand, price, quantity, is_active
    )
    return add_product_use_case.execute()
