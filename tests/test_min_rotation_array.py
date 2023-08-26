import pytest

from binary_search.min_roration_array import get_min_after_rotating_array


pytestmark = pytest.mark.minrotationarray


def test_get_min_after_rotating_array():
    assert 1 == get_min_after_rotating_array(input=[3, 4, 5, 1, 2])
    assert 0 == get_min_after_rotating_array(input=[4, 5, 6, 7, 0, 1, 2])
    assert 11 == get_min_after_rotating_array(input=[11, 13, 15, 17])
    assert 0 == get_min_after_rotating_array(input=[5, 6, 7, 0, 1, 2, 4])
