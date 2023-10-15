from functools import lru_cache


@lru_cache(maxsize=None)
def factorial(n: int):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


assert 120 == factorial(5)
assert 1 == factorial(0)
assert 2 == factorial(2)
