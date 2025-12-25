from praktikum.burger import Burger
import pytest
from praktikum.ingredient import Ingredient

class TestBurger:
    def test_burger_init(self):
        burger = Burger()
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    @pytest.mark.parametrize("bun_price, ingredient_names, expected_price", [
        (20, ["Tomato", "Lettuce"], 60),  # Пример: две булочки по 20 и ингредиенты по 10 и 5
        (25, ["Beef"], 70),              # Пример: две булочки по 25 и ингредиент по 20
    ])
    def test_get_price(self, burger, mock_bun, bun_price, ingredient_names, expected_price):
        mock_bun.get_price = lambda: bun_price  # Настраиваем метод get_price у mock_bun
        burger.set_buns(mock_bun)
        for ingredient_name in ingredient_names:
            if ingredient_name == "Beef":
                burger.add_ingredient(Ingredient("meat", ingredient_name, 20))
            else:
                burger.add_ingredient(Ingredient("vegetable", ingredient_name, 10))
        assert burger.get_price() == expected_price

    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun
        assert burger.get_price() == bun.get_price() * 2

    def test_move_ingredient(self, burger):
        # Добавляем несколько ингредиентов в бургер
        burger.add_ingredient(Ingredient("Tomato", "vegetable", 10))
        burger.add_ingredient(Ingredient("Lettuce", "vegetable", 5))
        burger.add_ingredient(Ingredient("Beef", "meat", 20))

        # Перемещаем ингредиент на первое место
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].get_name() == "vegetable"

        # Перемещаем ингредиент на последнее место
        burger.move_ingredient(0, 2)
        assert burger.ingredients[2].get_name() == "vegetable"