import pytest
from blind_75.two_ptrs.two_ptrs_problems import is_palindrome, three_sum,container_with_most_water

pytestmark = pytest.mark.twoptrsproblems


def test_valid_palindrome():
    # https://leetcode.com/problems/valid-palindrome/submissions/1144361720/
    assert True == is_palindrome(s="A man, a plan, a canal: Panama")


def test_three_sum():
    assert [[-1, -1, 2], [-1, 0, 1]] == three_sum(nums=[-1, 0, 1, 2, -1, -4])

def test_container_with_most_water():
    assert 49 == container_with_most_water(height=[1,8,6,2,5,4,8,3,7])
