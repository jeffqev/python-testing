import requests

from .calculator import Calculator

class Payroll:
    def calculate_salary(self, salary, bonus, taxes):
        calculator = Calculator()
        
        sub_total_salary = calculator.add(salary, bonus)

        return calculator.divide(sub_total_salary, taxes)
    
    def calculate_liquidation(self, employee_id, salary):
        calculator = Calculator()

        months_worked = self.get_employee_data(employee_id)['months_worked']

        return calculator.add(salary, salary * months_worked)
                   
    def get_employee_data(self, employee_id: int):

        response = requests.get(f"https://api.example.com/salary/{employee_id}")
        return response.json()
    