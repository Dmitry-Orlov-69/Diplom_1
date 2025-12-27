from praktikum.burger import Burger
import pytest
from praktikum.ingredient import Ingredient

class TestBurger:
    def test_burger_init(self):
        burger = Burger()
        assert burger.bun is None
        assert len(burger.ingredients) == 0

    def test_get_price_with_vegetables(self, burger, mock_bun):
        mock_bun.get_price = lambda: 20  # Настраиваем метод get_price у mock_bun
        burger.set_buns(mock_bun)
        burger.add_ingredient(Ingredient("vegetable", "Tomato", 10))
        burger.add_ingredient(Ingredient("vegetable", "Lettuce", 5))
        assert burger.get_price() == 55

    def test_get_price_with_meat(self, burger, mock_bun):
        mock_bun.get_price = lambda: 25  # Настраиваем метод get_price у mock_bun
        burger.set_buns(mock_bun)
        burger.add_ingredient(Ingredient("meat", "Beef", 20))
        assert burger.get_price() == 70


    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun
        assert burger.get_price() == bun.get_price() * 2

    def test_move_ingredient_to_first_place(self, burger):
        # Добавляем несколько ингредиентов в бургер
        burger.add_ingredient(Ingredient("Tomato", "vegetable", 10))
        burger.add_ingredient(Ingredient("Lettuce", "vegetable", 5))
        burger.add_ingredient(Ingredient("Beef", "meat", 20))

        # Перемещаем ингредиент на первое место
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0].get_name() == "vegetable"

    def test_move_ingredient_to_last_place(self, burger):
        # Добавляем несколько ингредиентов в бургер
        burger.add_ingredient(Ingredient("Tomato", "vegetable", 10))
        burger.add_ingredient(Ingredient("Lettuce", "vegetable", 5))
        burger.add_ingredient(Ingredient("Beef", "meat", 20))

        # Перемещаем ингредиент на последнее место
        burger.move_ingredient(0, 2)
        assert burger.ingredients[2].get_name() == "vegetable"