from pytest_mock import MockFixture

from app import Payroll
from app.calculator import Calculator

def test_calculate_salary_calculate_the_salary_when_data_is_correct(): 
    salary = 1000
    bonus = 100
    taxes = 2
    expected_salary = (salary + bonus) / taxes
    payroll = Payroll()

    actual_salary = payroll.calculate_salary(salary, bonus, taxes)
    
    assert actual_salary == expected_salary


def test_calculate_salary_calls_the_calculator_functions(mocker: MockFixture): 
    salary = 1000
    bonus = 100
    taxes = 2
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