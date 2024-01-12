import pytest
from blind_75.two_ptrs.two_ptrs_problems import is_palindrome

pytestmark = pytest.mark.twoptrsproblems


def test_valid_palindrome():
    # https://leetcode.com/problems/valid-palindrome/submissions/1144361720/
    assert True == is_palindrome(s="A man, a plan, a canal: Panama")
