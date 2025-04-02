import unittest
from leetcode.core.segment_tree import SegmentTree

class TestSegmentTree(unittest.TestCase):

    def test_range_query(self):
        nums = [1, 3, 5, 7, 9, 11]
        st = SegmentTree(nums)
        self.assertEqual(st.range_query(1, 3), 8)  # Sum of nums[1:3] = 3 + 5
        self.assertEqual(st.range_query(0, 6), 36)  # Sum of all elements

    def test_update(self):
        nums = [1, 3, 5, 7, 9, 11]
        st = SegmentTree(nums)
        st.update(1, 10)  # Update nums[1] to 10
        self.assertEqual(st.range_query(1, 3), 15)  # Sum of nums[1:3] = 10 + 5
        self.assertEqual(st.range_query(0, 6), 43)  # Updated total sum

if __name__ == "__main__":
    unittest.main()