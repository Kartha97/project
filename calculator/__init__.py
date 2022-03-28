""" This is the Calculator Class"""
from calculator.operations import Addition, Subtraction, Multiplication, Division


class Calculator(Addition, Subtraction, Multiplication, Division):
    """ This is the default result property"""
    def __init__(self):
        self._result = 0

    def add(self, value_1, value_2):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        self.set_result(Addition.add(value_1, value_2))
        return self.get_result()

    def subtract(self, value_1, value_2):
        """ This is the subtract method"""
        self.set_result(value_1 - value_2)
        return self.get_result()

    def multiply(self, value_1, value_2):
        """ This is the multiply method"""
        self.set_result(Multiplication.multiply(value_1, value_2))
        return self.get_result()

    def divide(self, value_1, value_2):
        """ This is the divide method"""
        self.set_result(Division.divide(value_1, value_2))
        return self.get_result()

    def set_result(self, value):
        """ This method is used to set value to the result private attribute"""
        self._result = value

    def get_result(self):
        """ This is the get result method"""
        return self._result