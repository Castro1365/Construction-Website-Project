import unittest

# Function to test
def get_max(a, b):
    return a if a > b else b

class TestGetMax(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(get_max(10, 5), 10)

    def test_negative_numbers(self):
        self.assertEqual(get_max(-1, -5), -1)

    def test_equal_numbers(self):
        self.assertEqual(get_max(7, 7), 7)

if __name__ == "__main__":
    unittest.main()
