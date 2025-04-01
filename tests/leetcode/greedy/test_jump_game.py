import unittest
from leetcode.greedy.jump_game import can_jump

class TestJumpGame(unittest.TestCase):
    def test_example_case(self):
        self.assertTrue(can_jump([2,3,1,1,4]))

    def test_cannot_reach(self):
        self.assertFalse(can_jump([3,2,1,0,4]))

    def test_single_element(self):
        self.assertTrue(can_jump([0]))

if __name__ == "__main__":
    unittest.main()