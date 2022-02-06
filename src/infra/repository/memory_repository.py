from datetime import datetime
from typing import Dict, List

from src.domain.entity.products import Products
from src.domain.repository.products_repository import ProductsRepository


class MemoryProductsRepository(ProductsRepository):
    def __init__(self) -> None:
        self.products = []

    def get_products(self) -> List[Products]:
        return self.products

    def add_product(self, product: Products) -> Dict:
        product_model = product.__dict__ | {
            "id": len(self.products) + 1,
            "created_at": datetime.now(),
            "updated_at": datetime.now(),
        }
        self.products.append(product_model)
        return product_model
