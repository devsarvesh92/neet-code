from linked_list.ll import Node, LinkedList


def reorder_linked_list(*, ll: LinkedList) -> Node:
    slow, fast = ll.head, ll.head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    start_second_half = slow.next
    slow.next = None

    first_list = ll

    # reverse 2nd half
    prev, curr = start_second_half, start_second_half.next
    prev.next = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    first, second = ll.head, prev
    while second:
        fnxt = first.next
        snext = second.next
        first.next = second
        second.next = fnxt
        first = fnxt
        second = snext


if __name__ == "__main__":
    ll = LinkedList()
    for n in [1, 2, 3, 4]:
        ll.insert_at_end(n)

    reorder_linked_list(ll=ll)
    print(ll)

    ll = LinkedList()

    for n in [1, 2, 3, 4, 5]:
        ll.insert_at_end(n)

    reorder_linked_list(ll=ll)
    print(ll)
