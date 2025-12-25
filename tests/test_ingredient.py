from praktikum.ingredient import Ingredient
import pytest

class TestIngredient:
    @pytest.mark.parametrize("ingredient_name, ingredient_type, ingredient_price", [
        ("Tomato", "vegetable", 10),
        ("Lettuce", "vegetable", 5),
        ("Beef", "meat", 20)
    ])
    def test_add_ingredient(self, burger, mock_ingredient, ingredient_name, ingredient_type, ingredient_price):
        mock_ingredient.configure_mock(name=ingredient_name, type=ingredient_type, price=ingredient_price)
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_remove_last_ingredient(self, burger):
        ingredient = Ingredient("Tomato", "vegetable", 10)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_non_existent_ingredient(self, burger):
        with pytest.raises(IndexError):
            burger.remove_ingredient(100)