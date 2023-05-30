import pytest
from pytest_mock import MockFixture

from app import Calculator

@pytest.mark.parametrize("number_1, number_2, expected_result", [
    (1, 1, 2),
    (2, 2, 4),
    (3, 3, 6),
    (4, 4, 8),
])
def test_addition_returns_the_correct_result_when_two_number_are_passed(number_1, number_2, expected_result ):
    #Arrange
    calculator = Calculator()

    #Act
    actual_result = calculator.add(number_1, number_2)

    #Assert
    assert  actual_result == expected_result

def test_division_returns_the_correct_result_when_two_number_are_passed():
    number_1 = 4
    number_2 = 2
    expected_result = 2
    calculator = Calculator()

    actual_result = calculator.divide(number_1, number_2)

    assert actual_result == expected_result

def test_division_raises_an_exception_when_is_divided_by_zero(mocker: MockFixture):
    calculator = Calculator()
    log = mocker.patch('app.logs.logging_msg')

    with pytest.raises(ValueError) as exception_info:
        calculator.divide(4, 0)
        
        assert str(exception_info) == "Can not divide by zero!"
        log.assert_called_once_with("Can not divide by zero!")