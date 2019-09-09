def consecutive_numbers(n: int) -> list:
    """
    Returns a list of lists of incremental numbers up to n in the format:
    [[1], [1, 2], [1, 2, n]]
    """

    return [list(range(1, x + 1)) for x in range(1, n + 1)]
