from typing import Self


class MinStack:
    def __init__(self) -> None:
        self._stack: list[int] = []
        self.min_value: list[int] = []

    def push(self: Self, val: int) -> None:
        self._stack.append(val)
        min_value = min(val, self.min_value[-1] if self.min_value else val)
        self.min_value.append(min_value)

    def pop(self: Self) -> None:
        self._stack.pop()
        self.min_value.pop()

    def top(self: Self) -> int:
        return self._stack[-1] if self._stack else None

    def get_min(self: Self) -> int:
        return self.min_value[-1]


if __name__ == "__main__":
    minStack = MinStack()
    print(minStack.push(-2))
    print(minStack.push(0))
    print(minStack.push(-3))
    print(minStack.get_min())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.get_min())
