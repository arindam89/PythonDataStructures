import unittest
from src.leetcode.intervals.meeting_rooms_ii import min_meeting_rooms

class TestMeetingRoomsII(unittest.TestCase):
    def test_min_meeting_rooms(self):
        self.assertEqual(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]), 2)
        self.assertEqual(min_meeting_rooms([[7, 10], [2, 4]]), 1)
        self.assertEqual(min_meeting_rooms([]), 0)
        self.assertEqual(min_meeting_rooms([[1, 5], [8, 9], [8, 9]]), 2)
        self.assertEqual(min_meeting_rooms([[1, 10], [2, 6], [5, 15]]), 3)

if __name__ == "__main__":
    unittest.main()