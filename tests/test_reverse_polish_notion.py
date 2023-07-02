import pytest
from stack.reverse_polish_notion import rpn


@pytest.mark.parametrize(
    "input,expected",
    [
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_revers_polish_notion(input, expected):
    assert rpn(input) == expected
