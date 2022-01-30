from src.domain.use_cases.get_products import GetProducts
from src.infra.repository.memory_repository import MemoryProductsRepository


def get_products_controller():
    mem_repository = MemoryProductsRepository()
    get_produtcs_use_case = GetProducts(mem_repository)
    return get_produtcs_use_case.execute()
