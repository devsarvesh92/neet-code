import pytest

from binary_search.search_in_asc import bianry_search


pytestmark = pytest.mark.binarysearch


def test_search_number_in_asc():
    input = [-1, 0, 3, 5, 9, 12]
    assert 4 == bianry_search(input=input, target=9)
