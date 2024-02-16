import pytest

from blind_75.linked_list.linked_list_problems import (
    LinkedList,
    merge_sorted_list,
    reverse_linked_list,
)


pytestmark = pytest.mark.linklistproblems


def test_merge_sorted_list():
    ll1 = LinkedList()
    for val in [1, 2, 4]:
        ll1.insert_at_end(val=val)

    ll2 = LinkedList()
    for val in [1, 3, 4]:
        ll2.insert_at_end(val=val)

    assert [1, 1, 2, 3, 4, 4] == merge_sorted_list(ll1=ll1, ll2=ll2)


def test_reverse_linked_list():
    ll1 = LinkedList()
    for val in [1, 2, 3, 4]:
        ll1.insert_at_end(val=val)
    expected_ll = LinkedList()
    for val in [4, 3, 2, 1]:
        expected_ll.insert_at_end(val=val)
    actual = reverse_linked_list(ip=ll1)
    res = actual == expected_ll
    assert res is True
