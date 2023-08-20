import pytest

from binary_search.search_in_matrix import search_matrix


pytestmark = pytest.mark.searchinmatrix


def test_search_in_matrix():
    assert True == search_matrix(
        input=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3
    )

    assert False == search_matrix(
        input=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=100
    )
