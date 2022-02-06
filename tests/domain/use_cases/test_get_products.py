from src.domain.entity.products import Products
from src.domain.use_cases.add_product import AddProduct
from src.domain.use_cases.get_products import GetProducts


def test_get_products(memory_repo):
    get_products_use_case = GetProducts(memory_repo)
    products = get_products_use_case.execute()
    assert products == []

    product = Products(
        name="fake",
        description="fake",
        brand="fake",
        price=0.0,
        quantity=0,
        is_active=True,
    )
    added_product = AddProduct(memory_repo, **product.__dict__).execute()

    products = get_products_use_case.execute()
    assert products == [added_product]
    assert len(products) == 1
