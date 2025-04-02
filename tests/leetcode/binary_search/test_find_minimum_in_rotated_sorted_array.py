import unittest
from src.leetcode.binary_search.find_minimum_in_rotated_sorted_array import find_min

class TestFindMin(unittest.TestCase):
    def test_rotated_array(self):
        self.assertEqual(find_min([3, 4, 5, 1, 2]), 1)

    def test_not_rotated_array(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)

    def test_single_element(self):
        self.assertEqual(find_min([1]), 1)

    def test_two_elements(self):
        self.assertEqual(find_min([2, 1]), 1)

    def test_large_rotation(self):
        self.assertEqual(find_min([4, 5, 6, 7, 0, 1, 2]), 0)

if __name__ == "__main__":
    unittest.main()