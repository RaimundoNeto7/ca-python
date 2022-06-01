from src.domain.use_cases.add_product import AddProduct
from src.domain.use_cases.get_products import GetProducts


class ProductsController:
    def __init__(self, repository) -> None:
        self.repository = repository

    def get_products_controller(self):
        get_produtcs_use_case = GetProducts(self.repository)
        return get_produtcs_use_case.execute()

    def add_product_controller(
        self, name, description, brand, price, quantity, is_active
    ):
        add_product_use_case = AddProduct(
            self.repository,
            name,
            description,
            brand,
            price,
            quantity,
            is_active,
        )
        return add_product_use_case.execute()
