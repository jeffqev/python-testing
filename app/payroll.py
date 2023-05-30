from .calculator import Calculator

class Payroll:
    def calculate_salary(self, salary, bonus, taxes):
        calculator = Calculator()

        sub_total_salary = calculator.add(salary, bonus)

        return calculator.divide(sub_total_salary, taxes)
     