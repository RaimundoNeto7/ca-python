from abc import ABC, abstractmethod
from typing import Dict, List

from src.domain.entity.products import Products


class ProductsRepository(ABC):
    @abstractmethod
    def get_products(self) -> List[Products]:
        raise NotImplementedError

    @abstractmethod
    def add_product(self, product: Products) -> Dict:
        raise NotImplementedError
