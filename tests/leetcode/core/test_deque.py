import unittest
from leetcode.core.deque import Deque

class TestDeque(unittest.TestCase):

    def test_add_front(self):
        dq = Deque()
        dq.add_front(1)
        dq.add_front(2)
        dq.add_front(3)
        self.assertEqual(str(dq), "[3, 2, 1]")

    def test_add_rear(self):
        dq = Deque()
        dq.add_rear(1)
        dq.add_rear(2)
        dq.add_rear(3)
        self.assertEqual(str(dq), "[1, 2, 3]")

    def test_delete_front(self):
        dq = Deque()
        dq.add_rear(1)
        dq.add_rear(2)
        dq.add_rear(3)
        self.assertEqual(dq.delete_front(), 1)
        self.assertEqual(str(dq), "[2, 3]")

    def test_delete_rear(self):
        dq = Deque()
        dq.add_rear(1)
        dq.add_rear(2)
        dq.add_rear(3)
        self.assertEqual(dq.delete_rear(), 3)
        self.assertEqual(str(dq), "[1, 2]")

    def test_is_empty(self):
        dq = Deque()
        self.assertTrue(dq.is_empty())
        dq.add_rear(1)
        self.assertFalse(dq.is_empty())

if __name__ == "__main__":
    unittest.main()