import math
import pytest

from src.calculations import area_of_circle, get_nth_fibonacci

def test_area_of_circle_positive():
    assert math.isclose(area_of_circle(1), math.pi, rel_tol=1e-9)
    assert math.isclose(area_of_circle(2.5), math.pi * 2.5 ** 2, rel_tol=1e-9)

def test_area_of_circle_negative_raises():
    with pytest.raises(ValueError) as exc:
        area_of_circle(-1)
    assert "Radius cannot be negative" in str(exc.value)

def test_get_nth_fibonacci_base_cases():
    assert get_nth_fibonacci(0) == 0
    assert get_nth_fibonacci(1) == 1

def test_get_nth_fibonacci_sequence():
    assert get_nth_fibonacci(2) == 1
    assert get_nth_fibonacci(3) == 2
    assert get_nth_fibonacci(10) == 55

def test_get_nth_fibonacci_negative_raises():
    with pytest.raises(ValueError) as exc:
        get_nth_fibonacci(-5)
    assert "n cannot be negative" in str(exc.value)
