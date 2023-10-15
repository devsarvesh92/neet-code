from functools import lru_cache


@lru_cache(maxsize=None)
def fibb(n: int) -> int:
    if n <= 2:
        return 1
    return fibb(n - 2) + fibb(n - 1)


def infinite_fibb():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


for x in infinite_fibb():
    print(x)

print(fibb(5))
