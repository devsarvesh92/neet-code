import gc
from typing import Any


class Node:
    def __init__(self, *, data: Any, next) -> None:
        self.data = data
        self.next = next


class LinkedList:
    """
    Linked list

    Big O Complexities:

    Insert at the beg: O(1)

    Insert at the end: O(n)
    Insert at the middle: O(n)

    Search: O(n)
    """

    def __init__(self) -> None:
        self.head = None

    def insert_at_beginning(self, data) -> None:
        node = Node(data=data, next=self.head)
        self.head = node

    def insert_at_end(self, data) -> None:
        if self.head is None:
            self.insert_at_beginning(data=data)
            return

        itr = self.head
        last_node = None

        while itr:
            last_node = itr
            itr = itr.next
        node = Node(data=data, next=None)
        last_node.next = node

    def insert_at(self, index, data):
        itr = self.head
        counter = 0
        while itr:
            if index < 1:
                raise ValueError("Index can't be negative")
            if index == 0:
                self.insert_at_beginning(data=data)

            if counter == index - 1:
                node = Node(data=data, next=itr.next)
                itr.next = node
                break

            itr = itr.next
            counter += 1

    def extend(self, values: list[Any]) -> None:
        for val in values:
            self.insert_at_end(data=val)

    def remove_from_beg(self):
        self.head = self.head.next
        gc.collect()

    def remove_at(self, index):
        itr = self.head
        counter = 0
        while itr:
            if index == 0:
                self.remove_from_beg()
            if index <= 0:
                raise ValueError("Index cant be less than 0")

            if counter == index - 1:
                itr.next = itr.next.next
                break

            counter += 1
            itr = itr.next

    def __str__(self) -> str:
        itr = self.head
        content = ""
        while itr:
            content = f"{content}->{itr.data}" if content else f"{itr.data}"
            itr = itr.next
        return content

    def __len__(self) -> int:
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next
        return counter


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning("sawant")
    ll.insert_at_beginning("sarvesh")
    ll.insert_at_end("prakash")
    ll.extend(["1", "2", "3"])
    ll.insert_at(index=1, data="wtf")
    ll.remove_at(index=1)

    print(ll)
    print(len(ll))
