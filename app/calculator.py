from .logs import logging_msg

class Calculator:
    def add(self, num_1: int, num_2: int) -> int:
        return num_1 + num_2
    
    def divide(self, num_1: int, num_2: int) -> int:
        if num_2 == 0:
            logging_msg("Can not divide by zero!")
            raise ValueError("Can not divide by zero!")

        return num_1 / num_2
