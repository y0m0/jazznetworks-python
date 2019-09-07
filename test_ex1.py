from ex1 import sum_of_multiples_div_by_3

def test_with_limit_0():
    limit = 0
    m = 3
    assert sum_of_multiples_div_by_3(limit, m) == 0

