from dataclasses import dataclass
from typing import TypeVar


Node = TypeVar("Node")


@dataclass
class Node:
    val: str
    nxt: Node


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_beg(self, val) -> None:
        self.head = Node(val=val, nxt=self.head)

    def insert_at_end(self, val) -> None:
        if self.head is None:
            self.insert_at_beg(val=val)
            return

        nxt_node = self.head

        while nxt_node:
            current_node = nxt_node
            nxt_node = nxt_node.nxt

        current_node.nxt = Node(val=val, nxt=current_node.nxt)

    def extend(self, ll) -> None:
        nxt = ll
        while nxt:
            self.insert_at_end(nxt.val)
            nxt = nxt.nxt

    def __str__(self) -> str:
        nxt_node = self.head
        nodes = f""
        while nxt_node:
            nodes = f"{nodes}->{nxt_node.val}"
            nxt_node = nxt_node.nxt
        return nodes


def merge_sorted_lists(l1: Node, l2: Node) -> LinkedList:
    l3 = LinkedList()

    while l1 and l2:
        if l1.val < l2.val:
            l3.insert_at_end(l1.val)
            l1 = l1.nxt
        else:
            l3.insert_at_end(l2.val)
            l2 = l2.nxt

    if l1:
        l3.extend(l1)
    elif l2:
        l3.extend(l2)
    return l3


if __name__ == "__main__":
    l1 = LinkedList()
    for x in [1, 2, 4]:
        l1.insert_at_end(x)
    print(str(l1))

    l2 = LinkedList()
    for x in [1, 3, 4]:
        l2.insert_at_end(x)
    print(str(l2))

    print(merge_sorted_lists(l1.head, l2=l2.head))
