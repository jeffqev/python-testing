import pytest
import typing

from faker import Faker
from pytest_mock import MockFixture

from app import Payroll
from app.calculator import Calculator

@pytest.fixture(name='salary_information')
def _salary_information(faker: Faker):
    salary = faker.pyint()
    bonus = faker.pyint()

    return {
        'salary': salary,
        'bonus': bonus,
        'taxes': salary + bonus,
    }

def test_calculate_salary_calculate_the_salary_when_data_is_correct(salary_information: typing.Dict): 
    _salary_information = salary_information
    expected_salary = (_salary_information['salary'] + _salary_information['bonus']) / _salary_information['taxes']
    payroll = Payroll()

    actual_salary = payroll.calculate_salary(
        _salary_information['salary'], 
        _salary_information['bonus'], 
        _salary_information['taxes']
    )
    
    assert actual_salary == expected_salary


def test_calculate_salary_calls_the_calculator_functions(mocker: MockFixture, salary_information: typing.Dict): 
    salary = salary_information['salary']
    bonus = salary_information['bonus']
    taxes = salary_information['taxes']
    expected_salary = (salary + bonus) / taxes
    add = mocker.patch('app.calculator.Calculator.add')
    add.return_value = salary + bonus
    divide = mocker.patch('app.calculator.Calculator.divide', return_value=expected_salary)
    payroll = Payroll()
    
    actual_salary = payroll.calculate_salary(salary, bonus, taxes)
    
    assert actual_salary == expected_salary
    add.assert_called_once_with(salary, bonus)
    divide.assert_called_once_with((salary + bonus), taxes)

def test_liquidation_returns_correct_liquidation(mocker: MockFixture):
    employee_id = 1
    salary = 1000
    months_worked = 12
    expected_liquidation = salary + (salary * months_worked)
    mock_employee_data = {'months_worked': months_worked}
    get_employee_data = mocker.patch('app.Payroll.get_employee_data')
    get_employee_data.return_value = mock_employee_data
    payroll = Payroll()

    liquidation_result = payroll.calculate_liquidation(employee_id, salary)

    assert liquidation_result == expected_liquidation
    get_employee_data.assert_called_once_with(employee_id)

def test_liquidation_raise_an_exception_when_there_are_not_months_worked(mocker: MockFixture):
    employee_id = 1
    salary = 1000
    mock_employee_data = {}
    get_employee_data = mocker.patch('app.Payroll.get_employee_data')
    get_employee_data.return_value = mock_employee_data
    payroll = Payroll()

    with pytest.raises(KeyError):
        payroll.calculate_liquidation(employee_id, salary)
        
        get_employee_data.assert_called_once_with(employee_id)