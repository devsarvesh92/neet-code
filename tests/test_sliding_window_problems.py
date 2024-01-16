import pytest

from blind_75.sliding_window.sliding_window_problems import max_profit

pytestmark = pytest.mark.slidingwindowproblems


def test_max_profit():
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1147929471/
    assert 5 == max_profit(prices=[7,1,5,3,6,4])
