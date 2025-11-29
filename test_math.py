import unittest


def pow(x, y):
    print(x, y)
    return x ** y

class TestPowFunction(unittest.TestCase):

    def test_positive_exponent(self):
        """Test pow with a normal positive exponent."""
        self.assertEqual(pow(2, 3), 8)

    def test_zero_exponent(self):
        """Test pow with exponent zero."""
        self.assertEqual(pow(5, 0), 1)

if __name__ == "__main__":
    unittest.main()
