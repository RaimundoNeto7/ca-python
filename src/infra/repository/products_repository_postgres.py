from typing import Dict, List

from sqlalchemy.orm.session import Session

from src.domain.entity.products import Products
from src.domain.repository.products_repository import ProductsRepository
from src.infra.database.config import get_db
from src.infra.database.models.products import Products as ProductsModel


class ProductsRepositoryPostgres(ProductsRepository):
    def __init__(self, session: Session) -> None:
        super().__init__()
        self.session = session

    def get_products(self) -> List[Products]:
        products = self.session.query(ProductsModel).all()
        return products

    def add_product(self, product: Products) -> Dict:
        product_db = ProductsModel(
            name=product.name,
            description=product.description,
            brand=product.brand,
            price=product.price,
            quantity=product.quantity,
        )

        self.session.add(product_db)
        self.session.commit()
        self.session.refresh(product_db)
        return product_db
