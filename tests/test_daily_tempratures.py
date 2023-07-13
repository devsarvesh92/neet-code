import pytest

from stack.daily_temp import daily_tempratures


pytestmark = pytest.mark.testdailytempratures


@pytest.mark.parametrize(
    "input,expected",
    [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ],
)
def test_daily_tempratures(input, expected):
    assert daily_tempratures(input=input) == expected
