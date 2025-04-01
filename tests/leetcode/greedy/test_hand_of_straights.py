import unittest
from leetcode.greedy.hand_of_straights import is_n_straight_hand

class TestHandOfStraights(unittest.TestCase):
    def test_example_case(self):
        self.assertTrue(is_n_straight_hand([1,2,3,6,2,3,4,7,8], 3))

    def test_invalid_case(self):
        self.assertFalse(is_n_straight_hand([1,2,3,4,5], 4))

    def test_single_group(self):
        self.assertTrue(is_n_straight_hand([1,2,3], 3))

if __name__ == "__main__":
    unittest.main()