import calculator
import pytest

def test_plus():
    object = calculator.four_function_calc()
    assert object.add(10, 20) == 30

def test_sub():
    object = calculator.four_function_calc()
    assert object.sub(20, 10) == 10

def test_mult1():
    object = calculator.four_function_calc()
    assert object.mult(10, 10) == 100

def test_mult2():
    object = calculator.four_function_calc()
    assert object.mult(-10, -10) != -100

def test_div1():
    object = calculator.four_function_calc()
    assert object.div(10, 10) == 1

def test_div2():
    object = calculator.four_function_calc()
    assert object.div(-10, -10) != -1