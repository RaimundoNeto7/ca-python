import pytest

from src.infra.repository.memory_repository import MemoryProductsRepository


@pytest.fixture
def memory_repo() -> MemoryProductsRepository:
    return MemoryProductsRepository()
