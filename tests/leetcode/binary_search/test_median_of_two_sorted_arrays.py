import unittest
from src.leetcode.binary_search.median_of_two_sorted_arrays import find_median_sorted_arrays

class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def test_even_total_length(self):
        self.assertEqual(find_median_sorted_arrays([1, 3], [2, 4]), 2.5)

    def test_odd_total_length(self):
        self.assertEqual(find_median_sorted_arrays([1, 3], [2]), 2.0)

    def test_one_empty_array(self):
        self.assertEqual(find_median_sorted_arrays([], [1]), 1.0)

    def test_both_empty_arrays(self):
        with self.assertRaises(ValueError):
            find_median_sorted_arrays([], [])

    def test_large_arrays(self):
        self.assertEqual(find_median_sorted_arrays([1, 2], [3, 4, 5, 6]), 3.5)

if __name__ == "__main__":
    unittest.main()