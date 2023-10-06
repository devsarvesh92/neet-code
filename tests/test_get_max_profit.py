import pytest

from sliding_window.profit_loss import get_max_profit


pytestmark = pytest.mark.slidingwindowmaxprofit


def test_get_max_profit():
    assert 5 == get_max_profit(prices=[7, 1, 5, 3, 6, 4])
    assert 0 == get_max_profit(prices=[7, 6, 4, 3, 1])
