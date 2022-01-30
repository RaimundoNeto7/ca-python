from abc import ABC, abstractmethod
from typing import List

from src.domain.entity.products import Products


class ProductsRepository(ABC):
    @abstractmethod
    def get_products(self) -> List[Products]:
        raise NotImplementedError
