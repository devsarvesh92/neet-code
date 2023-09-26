from dataclasses import dataclass
from typing import Any, Optional
from typing import TypeVar

Node = TypeVar("Node")


@dataclass
class Node:
    key: str
    val: Any
    prev: Node | None
    next: Node | None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0, None, None)
        self.right = Node(0, 0, None, None)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key):
        if key in self.cache:
            node: Node = self.cache[key]
            # Remove this from LL
            self._remove(node)

            # Add this at the beginning
            self._insert(node=node)

            return node

        return -1

    def put(self, key, val):
        if key in self.cache:
            node = self.get(key=key)
            node.val = val

        node = Node(key=key, val=val, prev=None, next=None)
        self._insert(node=node)
        self.cache[key] = node

        # check capacity
        if len(self.cache.keys()) > self.capacity:
            lru_node = self.left.next
            self._remove(node=lru_node)
            del self.cache[lru_node.key]

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node: Node):
        current_mru = self.right.prev

        current_mru.next = node
        node.prev = current_mru

        self.right.prev = node
        node.next = self.right

    def __str__(self) -> str:
        elments = ""
        nxt = self.left.next
        while nxt:
            elments = f"{elments}->{nxt.val}"
            nxt = nxt.next
        return elments


if __name__ == "__main__":
    lru_cache = LRUCache(capacity=3)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    lru_cache.put(4, 4)
    lru_cache.get(2)
    lru_cache.put(5, 5)
    print(lru_cache)
