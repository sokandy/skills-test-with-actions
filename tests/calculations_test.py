# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402

# Example additional test
import unittest
from src.calculations import some_function

class TestCalculations(unittest.TestCase):
    def test_some_function(self):
        # Add comprehensive tests covering all logic branches
        self.assertEqual(some_function(...), ...)  # Provide actual cases

if __name__ == '__main__':
    unittest.main()

def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


# def test_get_nth_fibonacci_ten():
#     """Test with n=10."""
#     # Arrange
#     n = 10

#     # Act
#     result = get_nth_fibonacci(n)

#     # Assert
#     assert result == 55


def test_area_of_circle_negative_radius():
   """Test with a negative radius to raise ValueError."""
   # Arrange
   radius = -1

   # Act & Assert
   with pytest.raises(ValueError):
      area_of_circle(radius)


def test_get_nth_fibonacci_negative():
   """Test with a negative number to raise ValueError."""
   # Arrange
   n = -1

   # Act & Assert
   with pytest.raises(ValueError):
      get_nth_fibonacci(n)


def test_area_of_circle_negative_radius():
   """Test with a negative radius to raise ValueError."""
   # Arrange
   radius = -1

   # Act & Assert
   with pytest.raises(ValueError):
      area_of_circle(radius)


def test_get_nth_fibonacci_negative():
   """Test with a negative number to raise ValueError."""
   # Arrange
   n = -1

   # Act & Assert
   with pytest.raises(ValueError):
      get_nth_fibonacci(n)


