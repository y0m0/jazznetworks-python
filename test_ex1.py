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

def test_with_multiplier_1():
    limit = 10
    m = 1
    assert sum_of_multiples_divisible_by_3(limit, m) == 18

def test_sum_of_multiples_divisible_by_3():
    limit = 10
    m = 2
    assert sum_of_multiples_divisible_by_3(limit, m) == 6

def test_sum_of_multiples_divisible_by_3_less_then_103020():
    limit = 999990
    m = 2

    # calculate the biggest sum possibile if we assume that all multiples
    # of 3 less then 102030 are included
    num_of_m = 102030 - 3 / 3
    max_possible_sum_of_multiples = 3 * num_of_m * (num_of_m + 1) / 2

    assert sum_of_multiples_divisible_by_3(limit, m) <= max_possible_sum_of_multiples

def test_with_negative_limit():
    limit = -10
    m = 5
    assert sum_of_multiples_divisible_by_3(limit, m) == 0

def test_with_negative_multiplier():
    limit = 10
    m = -2
    assert sum_of_multiples_divisible_by_3(limit, m) == 0
