import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def mock_bun(name: str, price: float):
    bun = Mock()
    bun.get_name.return_value = name
    bun.get_price.return_value = price
    return bun

@pytest.fixture
def mock_ingredient(ingredient_type: str, name: str, price: float):
    ingredient = Mock()
    ingredient.get_type.return_value = ingredient_type
    ingredient.get_name.return_value = name
    ingredient.get_price.return_value = price
    return ingredient
