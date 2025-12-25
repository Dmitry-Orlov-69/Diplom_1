from praktikum.bun import Bun
import pytest

class TestBun:
    def test_bun_price(self, bun):
        assert bun.get_price() == bun.price