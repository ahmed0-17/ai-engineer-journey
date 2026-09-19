from calculator import add,multiply,divide
import pytest


def test_add():
    assert add(2, 3) == 5


def test_mutliply():
    assert multiply(3,2)==6    


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)    