import unittest
from leetcode.greedy.valid_parenthesis_string import check_valid_string

class TestValidParenthesisString(unittest.TestCase):
    def test_example_case(self):
        self.assertTrue(check_valid_string("(*)"))

    def test_invalid_case(self):
        self.assertFalse(check_valid_string("(*))("))

    def test_empty_string(self):
        self.assertTrue(check_valid_string(""))

if __name__ == "__main__":
    unittest.main()