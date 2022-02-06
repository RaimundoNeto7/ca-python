from src.domain.entity.products import Products
from src.domain.use_cases.add_product import AddProduct


def test_add_product(memory_repo):
    product = Products(
        name="fake",
        description="fake",
        brand="fake",
        price=0.0,
        quantity=0,
        is_active=True,
    )
    add_product_use_case = AddProduct(memory_repo, **product.__dict__)
    assert add_product_use_case.execute().__contains__("id")
