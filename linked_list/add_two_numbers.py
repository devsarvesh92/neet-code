from linked_list.ll import LinkedList, Node


def add_two_numbers(ll1: Node, ll2: Node) -> LinkedList:
    dummy = LinkedList()
    carry = 0

    while ll1 or ll2 or carry:
        num1 = ll1.data if ll1 else 0
        num2 = ll2.data if ll2 else 0

        res = num1 + num2 + carry
        unit = res % 10
        carry = (res - unit) // 10

        dummy.insert_at_end(data=unit)
        ll1 = ll1.next
        ll2 = ll2.next
    return dummy


if __name__ == "__main__":
    ll1 = LinkedList()
    for i in [2, 4, 3]:
        ll1.insert_at_end(i)

    ll2 = LinkedList()
    for i in [5, 6, 4]:
        ll2.insert_at_end(i)

    print(add_two_numbers(ll1.head, ll2.head))
