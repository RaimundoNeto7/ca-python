from pydantic import BaseModel


class ProductsSchema(BaseModel):
    name: str
    description: str
    brand: str
    price: float
    quantity: int
    is_active: bool
