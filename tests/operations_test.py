"""Testing the calculator operations """

from calculator.operations import Addition, Subtraction, Multiplication


def Factory(operation="add"):
    """Factory Method"""
    localizers = {
        "add": Addition,
        "substract": Subtraction,
        "multiply": Multiplication,
    }

    return localizers[operation]()

def test_calculator_operations_add():
    """Testing the Calculator"""
    assert Factory("add").add(1, 1) == 2


def test_calculator_operations_multiply():
    """Testing the Calculator"""
    assert Factory("multiply").multiply(1, 1) == 1
