from dataclasses import dataclass
from typing import TypeVar

N = TypeVar("N")


class Node:
    def __init__(self, val, nxt, prev) -> None:
        self.val = val
        self.next = nxt
        self.prev = prev


class Deque:
    def __init__(self) -> None:
        self.head = Node(val=-1, nxt=None, prev=None)
        self.tail = Node(val=-1, nxt=None, prev=None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.len = 0

    def isEmpty(self) -> bool:
        if self.len == 0:
            return True
        return False

    def append(self, value: int) -> None:
        last_node = self.tail.prev
        node = Node(val=value, nxt=self.tail, prev=last_node)
        self.tail.prev = node
        last_node.next = node
        self.len += 1

    def appendleft(self, value: int) -> None:
        first_node = self.head.next
        node = Node(val=value, nxt=first_node, prev=self.head)
        first_node.prev = node
        self.head.next = node
        self.len += 1

    def pop(self) -> int:
        if self.len == 0:
            return -1
        last_node = self.tail.prev
        scnd_last_node = last_node.prev

        val = last_node.val
        self.tail.prev = scnd_last_node
        scnd_last_node.next = self.tail

        del last_node
        return val

    def popleft(self) -> int:
        if self.len == 0:
            return -1
        first_node = self.head.next
        val = first_node.val

        self.head.next = first_node.next
        first_node.next.prev = self.head

        del first_node
        return val
