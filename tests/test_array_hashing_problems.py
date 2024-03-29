import pytest
from blind_75.array_hashing.array_hashing_problems import (
    check_duplicates,
    check_anagram,
    top_k_frequent_elements,
    two_sum,
    group_anagrams,
    array_product_except_self,
    bubble_sort,
    get_prime_numbers,
    validate_sudoku_board,
    get_longest_consecutive_sequence,
)

pytestmark = pytest.mark.array_hashing


def test_contains_duplicates():
    # Leetcode: https://leetcode.com/problems/contains-duplicate/submissions/1136850092/
    assert True == check_duplicates(nums=[1, 2, 3, 1])
    assert False == check_duplicates(nums=[1, 2, 3, 4])


def test_anagram():
    # Leetcode: https://leetcode.com/problems/valid-anagram/submissions/1136851392/
    assert True == check_anagram(s="anagram", t="nagaram")
    assert False == check_anagram(s="rat", t="car")


def test_two_sum():
    # Leetcode: https://leetcode.com/problems/two-sum/submissions/1136857349/
    assert [0, 1] == two_sum(nums=[2, 7, 11, 15], target=9)


def test_group_anagrams():
    # Leetcode: https://leetcode.com/problems/group-anagrams/submissions/1136848716
    assert [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]] == group_anagrams(
        input=["eat", "tea", "tan", "ate", "nat", "bat"]
    )


def test_top_k_frequent_elements():
    # https://leetcode.com/problems/top-k-frequent-elements/submissions/1136938469/
    assert [1, 2] == top_k_frequent_elements(nums=[1, 1, 1, 2, 2, 3], k=2)
    assert [1] == top_k_frequent_elements(nums=[1], k=1)
    assert [1, 2] == top_k_frequent_elements(nums=[1, 2], k=2)
    assert [0] == top_k_frequent_elements(nums=[3, 0, 1, 0], k=1)
    assert [-1, 2] == top_k_frequent_elements(nums=[4, 1, -1, 2, -1, 2, 3], k=2)


def test_array_product_except_self():
    # https://leetcode.com/problems/product-of-array-except-self/submissions/1137826462/
    assert [12, 16, 24, 48, 24] == array_product_except_self(nums=[4, 3, 2, 1, 2])


def test_bubble_sort():
    assert [1, 2, 3, 4, 5] == bubble_sort(nums=[4, 2, 1, 3, 5])


def test_prime_numbers():
    assert [1, 2, 3, 5, 7, 11] == get_prime_numbers(start=1, end=12)


def test_sudoku_board():
    # https://leetcode.com/problems/valid-sudoku/submissions/1142476379/
    assert True == validate_sudoku_board(
        board=[
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )

    assert True == validate_sudoku_board(
        board=[
            [".", "8", "7", "6", "5", "4", "3", "2", "1"],
            ["2", ".", ".", ".", ".", ".", ".", ".", "."],
            ["3", ".", ".", ".", ".", ".", ".", ".", "."],
            ["4", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", ".", "."],
            ["6", ".", ".", ".", ".", ".", ".", ".", "."],
            ["7", ".", ".", ".", ".", ".", ".", ".", "."],
            ["8", ".", ".", ".", ".", ".", ".", ".", "."],
            ["9", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
    )


def test_longest_consecutive_sequence():
    # https://leetcode.com/problems/longest-consecutive-sequence/submissions/1142576855/
    assert 4 == get_longest_consecutive_sequence(nums=[100, 4, 200, 1, 3, 2])
