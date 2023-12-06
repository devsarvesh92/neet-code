from dataclasses import dataclass
from typing import Any, Iterable, TypeVar


Node = TypeVar("Node")


@dataclass
class Node:
    val: Any
    next: Node


class LinkedList:
    def __init__(self) -> None:
        self.head = Node(val="Head", next=None)
        self.len = 0

    def get(self, idx: int) -> Any:
        if idx >= self.len:
            return -1
        head = self.head
        nxt = head.next
        curr_id = 0
        while nxt:
            if curr_id == idx:
                return nxt.val
            nxt = nxt.next
        return -1

    def insertHead(self, val: Any) -> None:
        n = Node(val=val, next=self.head.next)
        self.head.next = n

    def insertTail(self, val: Any) -> None:
        head = self.head
        nxt = head.next
        while nxt:
            curr = nxt
            nxt = nxt.next

        tail = Node(val=val, next=None)
        curr.next = tail

    def remove(self, index: int) -> bool:
        if index == 0:
            current_head_ptr = self.head.next
            self.head.next = current_head_ptr.next
            del current_head_ptr

        curr = self.head.next
        current_id = 0
        while curr:
            if current_id + 1 == index:
                nxt_el = curr.next
                curr.next = nxt_el.next
                del nxt_el

    def getValues(self) -> Iterable:
        curr = self.head.next
        while curr:
            yield curr.val
            curr = curr.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertHead(val=1)
    for x in ll.getValues():
        print(x)
