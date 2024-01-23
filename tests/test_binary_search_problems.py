import pytest
from blind_75.binary_search.binary_search_problems import search_element

pytestmark = pytest.mark.binarysearchproblems


def test_binary_search():
    assert 7 == search_element(nums=[1, 2, 3, 4, 5, 6, 7, 8], num=8)
