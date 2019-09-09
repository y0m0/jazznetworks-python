import pytest
from ex2 import consecutive_numbers

def test_with_n_0():
    assert consecutive_numbers(0) == []

def test_with_n_1():
    assert consecutive_numbers(1) == [[1]]

def test_with_n_3():
    assert consecutive_numbers(3) == [[1], [1,2], [1,2,3]]

def test_with_n_negative():
    assert consecutive_numbers(-3) == []

def test_with_n_as_float():
    """check that an exception is raised if a float number is passed instead of an int"""
    with pytest.raises(Exception):
        assert consecutive_numbers(2.5)
