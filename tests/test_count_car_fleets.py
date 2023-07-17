import pytest

from stack.count_car_fleets import count_car_fleets

pytestmark = pytest.mark.countcarfleets


@pytest.mark.parametrize(
    "target,position,speed,expected", [(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3)]
)
def test_count_car_fleets(target, position, speed, expected):
    assert count_car_fleets(target=target, position=position, speed=speed) == expected
