import math
import pytest
from src.calculations import area_of_circle, get_nth_fibonacci, add, some_missing_function

def test_area_of_circle_values():
    assert math.isclose(area_of_circle(1), math.pi)
    assert math.isclose(area_of_circle(2.5), math.pi * 2.5**2)

def test_area_of_circle_negative_raises():
    with pytest.raises(ValueError):
        area_of_circle(-0.1)

@pytest.mark.parametrize("n,expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (10, 55),
])
def test_get_nth_fibonacci(n, expected):
    assert get_nth_fibonacci(n) == expected

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_some_missing_function():
    # If some_missing_function is intended to return 42, assert it here.
    assert some_missing_function() == 42
