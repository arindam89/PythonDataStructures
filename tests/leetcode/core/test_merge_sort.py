import unittest
from leetcode.core.merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_sort(self):
        self.assertEqual(merge_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(merge_sort([3, 1, 4, 2]), [1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()