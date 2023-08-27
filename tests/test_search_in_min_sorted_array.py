import pytest

from binary_search.search_in_roatated_sorted_array import search


pytestmark = pytest.mark.searchinrotatedsortedearray


def test_search_in_rotated_sorted_array():
    assert 4 == search(input=[4, 5, 6, 7, 0, 1, 2], target=0)
    assert -1 == search(input=[4, 5, 6, 7, 0, 1, 2], target=3)
    assert -1 == search(input=[1], target=0)
