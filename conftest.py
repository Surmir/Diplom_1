import pytest
from unittest.mock import Mock
from tests.data import DataMock as DM
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = DM.BUN_NAME
    bun.get_price.return_value = DM.BUN_PRICE
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = DM.INGREDIENT_TYPE
    ingredient.get_name.return_value = DM.INGREDIENT_NAME
    ingredient.get_price.return_value = DM.INGREDIENT_PRICE
    return ingredient
