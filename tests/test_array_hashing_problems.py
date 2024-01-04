import pytest
from blind_75.array_hashing.array_hashing_problems import (
    check_duplicates,
    check_anagram,
    two_sum,
    group_anagrams,
)

pytestmark = pytest.mark.array_hashing


def test_contains_duplicates():
    assert True == check_duplicates(nums=[1, 2, 3, 1])
    assert False == check_duplicates(nums=[1, 2, 3, 4])


def test_anagram():
    assert True == check_anagram(s="anagram", t="nagaram")
    assert False == check_anagram(s="rat", t="car")


def test_two_sum():
    assert [0, 1] == two_sum(nums=[2, 7, 11, 15], target=9)


def test_group_anagrams():
    # Leetcode : https://leetcode.com/problems/group-anagrams/submissions/1136848716
    assert [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] == group_anagrams(
        input=["eat", "tea", "tan", "ate", "nat", "bat"]
    )
