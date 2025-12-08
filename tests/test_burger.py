import pytest
from data import DataTest as DT


class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        
        assert mock_bun == burger.bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)

        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, burger):
        burger.ingredients = DT.INGREDIENTS
        ingredient = burger.ingredients[0]
        burger.remove_ingredient(0)

        assert ingredient not in burger.ingredients

    def test_move_ingredient(self, burger):
        burger.ingredients = DT.INGREDIENTS
        ingredient_before = burger.ingredients[0]
        burger.move_ingredient(0, -1)
        ingredient_after = burger.ingredients[-2]

        assert ingredient_before == ingredient_after

    @pytest.mark.parametrize('bun_price, ingredient_prices, expected_price', DT.PRICE_PARAM)
    def test_get_price(self, burger, mock_bun, mock_ingredient, bun_price, ingredient_prices, expected_price):
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        actual_price = burger.get_price()

        assert actual_price == expected_price

    @pytest.mark.parametrize('bun_name, ingredients_data, expected_receipt', DT.RECEIPT_PARAM)
    def test_get_receipt(self, burger, mock_bun, mock_ingredient, bun_name, ingredients_data, expected_receipt):
        mock_bun.get_name.return_value = bun_name
        burger.set_buns(mock_bun)

        for name, type_ing, price in ingredients_data:
            mock_ingredient.get_name.return_value = name
            mock_ingredient.get_type.return_value = type_ing
            mock_ingredient.get_price.return_value = price
            burger.add_ingredient(mock_ingredient)

        actual_receipt = burger.get_receipt()

        assert actual_receipt == '\n'.join(expected_receipt)
