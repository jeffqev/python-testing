import pytest
from pytest_mock import MockFixture

from app import Calculator

def test_addition():
    calculator = Calculator()
    assert calculator.add(1, 1) == 2

def test_division():
    calculator = Calculator()
    assert calculator.divide(4, 2) == 2

