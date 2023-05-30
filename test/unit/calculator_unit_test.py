import pytest
from pytest_mock import MockFixture

from app import Calculator

def test_addition():
    calculator = Calculator()
    assert calculator.add(1, 1) == 2

def test_division():
    calculator = Calculator()
    assert calculator.divide(4, 2) == 2

def test_division_raises_exception(mocker: MockFixture):
    calculator = Calculator()

    log = mocker.patch('app.logs.logging_msg')

    with pytest.raises(ValueError) as exception_info:
        calculator.divide(4, 0)
        assert str(exception_info) == "Can not divide by zero!"
        log.assert_called_once_with("Can not divide by zero!")