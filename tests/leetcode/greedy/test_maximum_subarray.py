import unittest
from leetcode.greedy.maximum_subarray import max_subarray

class TestMaximumSubarray(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(max_subarray([-2,1,-3,4,-1,2,1,-5,4]), 6)

    def test_single_element(self):
        self.assertEqual(max_subarray([1]), 1)

    def test_all_negative(self):
        self.assertEqual(max_subarray([-1, -2, -3]), -1)

    def test_all_positive(self):
        self.assertEqual(max_subarray([1, 2, 3, 4]), 10)

if __name__ == "__main__":
    unittest.main()