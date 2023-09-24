import pytest

from linked_list.ll_reversal_problem import LinkedList


pytestmark = pytest.mark.reverselinklist


def test_reverse_linked_list():
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.insert_at_end(val=val)
    ll.reverse_using_two_ptrs()
    assert str(ll) == "->5->4->3->2->1"
