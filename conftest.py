from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
import pytest
from pytest_mock import MockerFixture

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def ingredient():
    return Ingredient("Tomato", "vegetable", 10)

@pytest.fixture
def bun():
    return Bun("Classic Bun", 20)

@pytest.fixture
def mock_ingredient(mocker):
    return mocker.Mock(spec=Ingredient)

@pytest.fixture
def mock_bun(mocker):
    return mocker.Mock(spec=Bun)