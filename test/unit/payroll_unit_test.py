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
