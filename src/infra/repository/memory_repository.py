from typing import List

from src.domain.entity.products import Products
from src.domain.repository.products_repository import ProductsRepository


class MemoryProductsRepository(ProductsRepository):
    def __init__(self) -> None:
        self.products = []
        self.products.extend(
            [
                Products(
                    name="name 1",
                    description="desc 1",
                    brand="brand 1",
                    price=10.0,
                    quantity=2,
                    is_active=True,
                ),
                Products(
                    name="name 2",
                    description="desc 2",
                    brand="brand 1",
                    price=5.0,
                    quantity=2,
                    is_active=True,
                ),
            ]
        )

    def get_products(self) -> List[Products]:
        return self.products
