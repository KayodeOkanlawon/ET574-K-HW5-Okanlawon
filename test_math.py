# test_math.py
# Name: Kayode Okanlawon
# QCC ID: 24615461

import my_math


def test_pow():
    assert my_math.pow(2, 3) == 8
    assert my_math.pow(5, 2) == 25
    assert my_math.pow(10, 0) == 1
    assert abs(my_math.pow(2, -3) - 0.125) < 1e-12


def test_factorial():
    assert my_math.factorial(5) == 120
    assert my_math.factorial(3) == 6
    assert my_math.factorial(0) == 1
    assert my_math.factorial(-4) == "Error: factorial is not defined for negative numbers."


def test_distance():
    assert abs(my_math.distance(0, 0, 3, 4) - 5) < 1e-12
    assert abs(my_math.distance(1, 2, 4, 6) - 5) < 1e-12
    assert my_math.distance(2, 3, 2, 3) == 0


if __name__ == "__main__":
    test_pow()
    test_factorial()
    test_distance()
    print("All tests passed successfully.")