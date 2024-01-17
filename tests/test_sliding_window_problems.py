import pytest

from blind_75.sliding_window.sliding_window_problems import (
    max_profit,
    longest_substring_without_rep_chars,
    longest_rep_char_replacement,
)

pytestmark = pytest.mark.slidingwindowproblems


def test_max_profit():
    # https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1147929471/
    assert 5 == max_profit(prices=[7, 1, 5, 3, 6, 4])


def test_longest_substring_without_rep_chars():
    assert 2 == longest_substring_without_rep_chars(input="aab")


def test_longest_rep_char_replacement():
    # https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1148968162/
    assert 4 == longest_rep_char_replacement(s="AABABBA", k=1)
