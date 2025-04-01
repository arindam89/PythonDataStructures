import unittest
from leetcode.greedy.jump_game_ii import jump

class TestJumpGameII(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(jump([2,3,1,1,4]), 2)

    def test_single_element(self):
        self.assertEqual(jump([0]), 0)

    def test_two_elements(self):
        self.assertEqual(jump([1,2]), 1)

if __name__ == "__main__":
    unittest.main()