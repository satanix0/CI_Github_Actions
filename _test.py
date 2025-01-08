import pytest

# This script contains functions to calculate the square, cube, and fifth power of a number.
# It also includes test cases for these functions using the pytest framework.

# Function to calculate the square of a number


def square(n):
    return n ** 2

# Function to calculate the cube of a number


def cube(n):
    return n ** 3

# Function to calculate the fifth power of a number


def fifth_power(n):
    return n ** 5

# Test cases for the square function


def test_square():
    assert square(2) == 4, "Test Failed: Square of 2 should be 4"
    assert square(3) == 9, "Test Failed: Square of 3 should be 9"

# Test cases for the cube functio


def test_cube():
    assert cube(2) == 8, "Test Failed: Cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: Cube of 3 should be 27"

# Test cases for the fifth power function


def test_fifth_power():
    assert fifth_power(2) == 32, "Test Failed:fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "Test Failed:fifth power of 3 should be 243"

# Test case to check handling of invalid input for the square function


def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
