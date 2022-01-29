import pytest

from src.domain.entity.products import Products


def test_products():
    product = Products("camisa", "camisa malha peruana", "adidas", 21.00, 10, True)
    expected = (
        "Products(name='camisa', "
        "description='camisa malha peruana', "
        "brand='adidas', "
        "price=21.0, "
        "quantity=10, "
        "is_active=True)"
    )
    assert product.__str__() == expected


@pytest.mark.parametrize(
    "price, quantity",
    [(1.0, -10), (-1.0, 10), (-1, -1), (-1.0, -1.0), (-0.999999999, 0.0)],
)
def test_products_with_error(price, quantity):
    with pytest.raises(ValueError):
        Products("camisa", "camisa malha peruana", "adidas", price, quantity, True)
