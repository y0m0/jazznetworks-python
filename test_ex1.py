import pytest
from ex1 import sum_of_multiples_divisible_by_3

def test_with_multiplier_0():
    limit = 10
    m = 0
    assert sum_of_multiples_divisible_by_3(10, 0) == 0

def test_with_limit_0():
    limit = 0
    m = 3
    assert sum_of_multiples_divisible_by_3(limit, m) == 0

def test_with_limit_1():
    limit = 1
    m = 2
    assert sum_of_multiples_divisible_by_3(limit, m) == 0
