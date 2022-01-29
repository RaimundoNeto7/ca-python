class Products:
    def __init__(
        self,
        name: str,
        description: str,
        brand: str,
        price: float,
        quantity: int,
        is_active: bool,
    ) -> None:
        if price < 0.0:
            raise ValueError("price should be non-negative real")

        if quantity < 0:
            raise ValueError("price should be non-negative integer")

        self.name = name
        self.description = description
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.is_active = is_active

    def __repr__(self) -> str:
        return (
            f"Products(name='{self.name}', "
            f"description='{self.description}', "
            f"brand='{self.brand}', "
            f"price={self.price}, "
            f"quantity={self.quantity}, "
            f"is_active={self.is_active})"
        )
