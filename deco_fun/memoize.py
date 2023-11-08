def memoize(func):
    memory = {}

    def wrapper(*args, **kwargs):
        if args in memory:
            print(f"Geeting it from memory for {args=}")
            return memory[args]
        else:
            result = func(*args)
            memory[args] = result
            return result

    return wrapper


@memoize
def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))
print(factorial(10))
