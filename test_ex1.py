import pytest
from ex1 import sum_of_multiples_divisible_by_3

def test_with_multiplier_0():
    limit = 10
    m = 0
    assert sum_of_multiples_divisible_by_3(10, 0) == 0
