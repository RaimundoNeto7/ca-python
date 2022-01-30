from src.domain.repository.products_repository import ProductsRepository


class GetProducts:
    def __init__(self, repository: ProductsRepository) -> None:
        self.repository = repository

    def execute(self):
        products = self.repository.get_products()
        return products
