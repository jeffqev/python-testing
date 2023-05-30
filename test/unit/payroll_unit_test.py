from pytest_mock import MockFixture

from app import Payroll
from app.calculator import Calculator

def test_calculate_salary (): 
    salary = 1000
    bonus = 100
    taxes = 2
    payroll = Payroll()
    result_salary = payroll.calculate_salary(salary, bonus, taxes)
    assert result_salary == (salary + bonus) / taxes


def test_calculate_salary_2 (mocker: MockFixture): 
    salary = 1000
    bonus = 100
    taxes = 2
    payroll = Payroll()
    add = mocker.patch('app.calculator.Calculator.add')
    add.return_value = salary + bonus
    divide = mocker.patch('app.calculator.Calculator.divide', return_value=(salary + bonus) / taxes)
    salary_result = payroll.calculate_salary(salary, bonus, taxes)
    assert salary_result == ((salary + bonus) / taxes)
    add.assert_called_once_with(salary, bonus)
    divide.assert_called_once_with((salary + bonus), taxes)

def test_liquidation(mocker: MockFixture):
    employee_id = 1
    salary = 1000
    months_worked = 12
    payroll = Payroll()
    get_employee_data = mocker.patch('app.Payroll.get_employee_data')
    get_employee_data.return_value = {'months_worked': months_worked}
    liquidation_result = payroll.calculate_liquidation(employee_id, salary)
    assert liquidation_result == (salary + (salary * months_worked))
    get_employee_data.assert_called_once_with(employee_id)