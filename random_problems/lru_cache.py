from dataclasses import dataclass
from typing import Any, TypeVar


NodeType = TypeVar("NodeType")


@dataclass
class Node:
    """_summary_"""

    val: Any
    left: NodeType
    right: NodeType
    key: str


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache: dict[str, Node] = {}
        self.capacity = capacity
        self.head = Node("", None, None, None)
        self.tail = Node("", None, None, None)
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key) -> Any:
        if key in self.cache:
            node = self.cache[key]
            val = node.val
            self._remove(node=node)
            del self.cache[key]

            node = Node(key=key, val=val, left=self.head.right, right=self.head.left)
            self._insert(node=node)

            self.cache[key] = node
        return val

    def set(self, key, val) -> Any:
        if len(self.cache) == self.capacity:
            lru_node: Node = self.tail.left
            self._remove(node=lru_node)
            del self.cache[lru_node.key]

        if key in self.cache:
            self._remove(node=self.cache[key])

        node = Node(key=key, val=val, right=self.head.right, left=self.head)
        self._insert(node=node)
        self.cache[key] = node

        return val

    def _insert(self, node: Node) -> Node:
        mru = self.head.right
        mru.left = node
        self.head.right = node

    def _remove(self, node: Node) -> None:
        prev, nxt = node.left, node.right
        if prev:
            prev.right = nxt
        if nxt:
            nxt.left = prev

    def __str__(self) -> str:
        elements = ""
        curr = self.head
        while curr.right:
            elements = f"{elements}->{curr.val}"
            curr = curr.right

        return elements


if __name__ == "__main__":
    lru_cache = LRUCache(capacity=2)
    lru_cache.set("name", "sarvesh")
    lru_cache.set("surname", "sawant")
    lru_cache.set("name1", "sarvesh1")
    print(lru_cache)
    print(lru_cache.get("name1"))
    lru_cache.set("name2", "sarvesh2")
