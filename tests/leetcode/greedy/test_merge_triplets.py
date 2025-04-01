import unittest
from leetcode.greedy.merge_triplets import merge_triplets

class TestMergeTriplets(unittest.TestCase):
    def test_example_case(self):
        self.assertTrue(merge_triplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5]))

    def test_invalid_case(self):
        self.assertFalse(merge_triplets([[1,3,4],[2,5,8]], [2,5,5]))

    def test_single_triplet(self):
        self.assertTrue(merge_triplets([[2,7,5]], [2,7,5]))

if __name__ == "__main__":
    unittest.main()