import unittest
from src.leetcode.binary_search.koko_eating_bananas import min_eating_speed

class TestMinEatingSpeed(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(min_eating_speed([3, 6, 7, 11], 8), 4)

    def test_single_pile(self):
        self.assertEqual(min_eating_speed([30], 5), 6)

    def test_large_piles(self):
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 5), 30)

    def test_exact_hours(self):
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 6), 23)

if __name__ == "__main__":
    unittest.main()