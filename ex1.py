def sum_of_multiples_divisible_by_3(limit, m):
    """
    Generate all multiples of m from 0 up to and including a given limit
    Then sum all multiples which are also divisible by 3 and less then 102030
    """

    # The only multiple of 0 is itself
    if m == 0:
        return 0
