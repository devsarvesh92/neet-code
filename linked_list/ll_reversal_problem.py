from dataclasses import dataclass
from typing import Any, Self, TypeVar

Node = TypeVar("Node")


@dataclass
class Node:
    val: Any
    next: Node


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self: Self, val: Any) -> None:
        node = Node(val=val, next=self.head)
        self.head = node

    def insert_at_end(self: Self, val: Any) -> None:
        if self.head is None:
            self.insert_at_beginning(val=val)
            return

        nxt_ptr = self.head
        while nxt_ptr:
            el = nxt_ptr
            nxt_ptr = nxt_ptr.next

        el.next = Node(val=val, next=None)

    def reverse(self: Self):
        # h -> 1 -> 2 - >3 -> 4 -> 5
        # h -> 5 -> 4 -> 3 -> 2 - > 1
        # ->5->4->3->2->1->1->2->3->4->5
        itr = self.head
        self.head = None
        while itr:
            self.insert_at_beginning(val=itr.val)
            itr = itr.next

    def reverse_using_two_ptrs(self):
        # h -> 1 -> 2 - >3 -> 4 -> 5
        prev, curr = None, self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def __str__(self) -> str:
        itr = self.head
        vals = ""
        while itr:
            vals = f"{vals}->{itr.val}"
            itr = itr.next

        return vals
