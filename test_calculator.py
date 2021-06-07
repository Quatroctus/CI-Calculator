"""
Tests for calculator.py
"""
from calculator import add, divide, multiply, subtract


class TestCalculator:

    def test_add(self):
        assert 5 == add(3, 2)

    def test_sub(self):
        assert 5 == subtract(10, 5)

    def test_mult(self):
        assert 25 == multiply(5, 5)

    def test_divide(self):
        assert 3 == divide(21, 7)
