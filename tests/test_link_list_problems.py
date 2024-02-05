import pytest

from blind_75.linked_list.linked_list_problems import LinkedList, merge_sorted_list


pytestmark = pytest.mark.reverselinklist


def test_reverse_linked_list():
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.insert_at_end(val=val)
    ll.reverse()
    assert str(ll) == "->5->4->3->2->1"


def test_merge_sorted_list():
    ll1 = LinkedList()
    for val in [1, 2, 4]:
        ll1.insert_at_end(val=val)

    ll2 = LinkedList()
    for val in [1, 3, 4]:
        ll2.insert_at_end(val=val)

    assert [1, 1, 2, 3, 4, 4] == merge_sorted_list(ll1=ll1, ll2=ll2)
