class Node:
    """
    Represents a node in a linked list.

    Attributes:
        nxt: The next node in the linked list.
        val: The value stored in the node.
    """

    def __init__(self, nxt, val) -> None:
        self.nxt = nxt
        self.val = val


class LinkedList:
    def __init__(
        self,
    ) -> None:
        self.head = Node(nxt=None, val=-1000)

    def insert_at_beginning(self, val: int) -> None:
        curr_head = self.head
        node = Node(nxt=curr_head.nxt, val=val)
        self.head.nxt = node

    def insert_at_end(self, val: int) -> None:
        if self.head.nxt is None:
            self.insert_at_beginning(val=val)
            return

        curr = self.head.nxt
        while curr:
            prev = curr
            curr = curr.nxt
        node = Node(val=val, nxt=None)
        prev.nxt = node

    def __str__(self) -> str:
        vals = ""
        curr = self.head.nxt

        while curr:
            vals = f"{vals}->{curr.val}"
            curr = curr.nxt
        return vals

    def reverse(self):
        prev, curr = None, self.head.nxt
        while curr:
            temp = curr.nxt
            curr.nxt = prev
            prev = curr
            curr = temp
        self.head.nxt = prev


def merge_sorted_list(ll1: LinkedList, ll2: LinkedList) -> list[int]:
    ll = LinkedList()
    ll1_curr: Node = ll1.head.nxt
    ll2_curr: Node = ll2.head.nxt
    curr = Node(nxt=None, val=-1000)
    ll.head = curr

    while ll1_curr or ll2_curr:
        if ll1_curr and ll2_curr:
            if ll1_curr.val < ll2_curr.val:
                curr.nxt = ll1_curr
                curr = ll1_curr
                ll1_curr = ll1_curr.nxt
            else:
                curr.nxt = ll2_curr
                curr = ll2_curr
                ll2_curr = ll2_curr.nxt
        elif ll1_curr:
            curr.nxt = ll1_curr
            curr = ll1_curr
            ll1_curr = ll1_curr.nxt
        elif ll2_curr:
            curr.nxt = ll2_curr
            curr = ll2_curr
            ll2_curr = ll2_curr.nxt

    curr = ll.head.nxt
    result = []
    while curr:
        result.append(curr.val)
        curr = curr.nxt
    return result
