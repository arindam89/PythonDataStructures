import unittest
from src.leetcode.binary_search.search_in_rotated_sorted_array import search

class TestSearchInRotatedSortedArray(unittest.TestCase):
    def test_target_found(self):
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 0), 4)

    def test_target_not_found(self):
        self.assertEqual(search([4, 5, 6, 7, 0, 1, 2], 3), -1)

    def test_single_element_found(self):
        self.assertEqual(search([1], 1), 0)

    def test_single_element_not_found(self):
        self.assertEqual(search([1], 2), -1)

    def test_two_elements(self):
        self.assertEqual(search([2, 1], 1), 1)

if __name__ == "__main__":
    unittest.main()