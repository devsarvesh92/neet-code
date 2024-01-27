import pytest
from blind_75.binary_search.binary_search_problems import (
    search_element,
    find_min,
    search_in_rotated_array,
)

pytestmark = pytest.mark.binarysearchproblems


def test_binary_search():
    assert 7 == search_element(nums=[1, 2, 3, 4, 5, 6, 7, 8], num=8)


def test_find_min():
    # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/1156667651/
    assert 1 == find_min(nums=[3, 4, 5, 1, 2])


def test_search_in_rotated_sorted_array():
    # https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1158552103/
    assert 1 == search_in_rotated_array(nums=[5, 1, 2, 3, 4], target=1)
