"""Testing the calculator operations """

from calculator.operations import Addition, Subtraction, Multiplication, Division


def Factory(operation="add"):
    """Factory Method"""
    localizers = {
        "add": Addition,
        "substract": Subtraction,
        "multiply": Multiplication,
        "divide": Division
    }

    return localizers[operation]()

def test_calculator_operations_add():
    """Testing the Calculator add"""
    assert Factory("add").add(1, 1) == 2


def test_calculator_operations_multiply():
    """Testing the Calculator multiply"""
    assert Factory("multiply").multiply(1, 1) == 1

def test_calculator_operations_divide():
    """Testing the Calculator divide"""
    assert Factory("divide").divide(1, 1) == 1
