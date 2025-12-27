from praktikum.ingredient import Ingredient

class TestGetReceipt:
    def test_get_receipt(self, burger, bun):
        burger.set_buns(bun)

        # Добавляем несколько ингредиентов
        ingredient1 = Ingredient("vegetable", "Tomato", 10)
        ingredient2 = Ingredient("vegetable", "Lettuce", 5)
        ingredient3 = Ingredient("meat", "Beef", 20)

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)

        expected_receipt = f"""
        (==== {bun.get_name()} ====)
        = vegetable Tomato =
        = vegetable Lettuce =
        = meat Beef =
        (==== {bun.get_name()} ====)\n
        Price: {burger.get_price()}
        """
        current_receipt = burger.get_receipt()
        assert current_receipt == expected_receipt.strip()