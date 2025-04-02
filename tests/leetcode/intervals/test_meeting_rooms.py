import unittest
from src.leetcode.intervals.meeting_rooms import can_attend_meetings

class TestMeetingRooms(unittest.TestCase):
    def test_can_attend_meetings(self):
        self.assertTrue(can_attend_meetings([[0, 30], [35, 50], [60, 70]]))
        self.assertFalse(can_attend_meetings([[0, 30], [25, 50], [60, 70]]))
        self.assertTrue(can_attend_meetings([]))
        self.assertTrue(can_attend_meetings([[5, 10]]))
        self.assertFalse(can_attend_meetings([[7, 10], [2, 4], [9, 12]]))

if __name__ == "__main__":
    unittest.main()