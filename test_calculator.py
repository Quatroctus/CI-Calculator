"""
Tests for calculator.py
"""
from calculator import *


class TestCalculator:

    def test_add(self):
        assert 5 == add(3, 2)

    def test_sub(self):
        assert 5 == subtract(10, 5)
