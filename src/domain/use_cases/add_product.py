from typing import Dict

from src.domain.entity.products import Products
from src.domain.repository.products_repository import ProductsRepository


class AddProduct:
    def __init__(
        self,
        repository: ProductsRepository,
        name: str,
        description: str,
        brand: str,
        price: float,
        quantity: int,
        is_active: bool,
    ) -> None:
        self.repository = repository
        self.product = Products(name, description, brand, price, quantity, is_active)

    def execute(self) -> Dict:
        return self.repository.add_product(self.product)
