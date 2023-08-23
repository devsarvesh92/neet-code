import pytest

from binary_search.koko_eating_bananas import get_min_rate_for_koko_eating_banana


pytestmark = pytest.mark.kokoeatingbananas


def test_koko_eating_banans():
    assert 4 == get_min_rate_for_koko_eating_banana(piles=[3, 6, 7, 11], h=8)
    assert 30 == get_min_rate_for_koko_eating_banana(piles=[30, 11, 23, 4, 20], h=6)
