import unittest
from src.leetcode.linked_list.find_the_duplicate_number import find_duplicate

class TestFindDuplicate(unittest.TestCase):
    def test_find_duplicate(self):
        # Test case 1: Normal case
        nums = [1, 3, 4, 2, 2]
        self.assertEqual(find_duplicate(nums), 2)

        # Test case 2: Duplicate at the start
        nums = [3, 1, 3, 4, 2]
        self.assertEqual(find_duplicate(nums), 3)

        # Test case 3: All elements are the same
        nums = [2, 2, 2, 2, 2]
        self.assertEqual(find_duplicate(nums), 2)

if __name__ == "__main__":
    unittest.main()