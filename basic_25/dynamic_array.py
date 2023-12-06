from typing import Any


class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.size:
            raise IndexError("Index out of bounds")
        self.arr[i] = n

    def pushback(self, n: Any) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        el = self.arr[self.size]
        return el

    def resize(self) -> None:
        arr = [None] * self.capacity * 2
        for id, el in enumerate(self.arr):
            arr[id] = el
        self.arr = arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def __str__(self) -> str:
        rep = ""
        for i in self.arr:
            rep = f"{rep}->{i}" if rep != "" else i

        return rep


if __name__ == "__main__":
    d = DynamicArray(2)
    d.pushback(1)
    d.pushback(2)
    print(d.get(0))
    print(d.get(1))
    print(d.set(1, 3))
    print(d.get(1))
    print(d.popback())
    print(d.get(0))
    print(d)
