""" These are the Operation Classes"""
from abc import ABC, abstractmethod

class Addition:
    """ This is the addition class"""
    # this defines a static method that you can use without instantiating the calculator class
    # If you can go to the store and buy it, it is an an object.  If you can't buy it then its a static method
    @staticmethod
    def add(value_1, value_2):
        """ This is the add method"""
        return value_1 + value_2

class Subtraction(ABC):
    """ This is the subtraction class"""
    @abstractmethod
    def subtract(self, value_1, value_2):
        """ This is the subtract method"""
        pass

class Multiplication:
    """ This is the Multiplication class"""

    @staticmethod
    def multiply(value_1, value_2):
        """ This is the multiply method"""
        return value_1 * value_2

class Division:
    """ This is the Division class"""

    @staticmethod
    def divide(value_1, value_2):
        """ This is the divide method"""
        return value_1 / value_2
