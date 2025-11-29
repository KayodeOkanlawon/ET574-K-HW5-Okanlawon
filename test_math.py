# test_math.py
# Name: Kayode Okanlawon
# QCC ID: 24615461

import unittest
import my_math

class TestMyMath(unittest.TestCase):

    # --- Tests for pow(x, y) ---
    def test_pow(self):
        self.assertEqual(my_math.pow(2, 3), 8)
        self.assertEqual(my_math.pow(5, 2), 25)
        self.assertEqual(my_math.pow(10, 0), 1)
        self.assertAlmostEqual(my_math.pow(2, -3), 0.125, places=12)

    # --- Tests for factorial(n) ---
    def test_factorial(self):
        self.assertEqual(my_math.factorial(5), 120)
        self.assertEqual(my_math.factorial(3), 6)
        self.assertEqual(my_math.factorial(0), 1)
        self.assertEqual(my_math.factorial(-4), "Error: factorial is not defined for negative numbers.")

    # --- Tests for distance(x1, y1, x2, y2) ---
    def test_distance(self):
        self.assertAlmostEqual(my_math.distance(0, 0, 3, 4), 5, places=12)
        self.assertAlmostEqual(my_math.distance(1, 2, 4, 6), 5, places=12)
        self.assertEqual(my_math.distance(2, 3, 2, 3), 0)

if __name__ == "__main__":
    unittest.main()
