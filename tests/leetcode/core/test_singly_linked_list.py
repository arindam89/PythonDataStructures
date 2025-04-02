import unittest
from leetcode.core.singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def test_add_at_head(self):
        sll = SinglyLinkedList()
        sll.add_at_head(1)
        sll.add_at_head(2)
        sll.add_at_head(3)
        self.assertEqual(str(sll), "3->2->1")

    def test_add_at_tail(self):
        sll = SinglyLinkedList()
        sll.add_at_tail(1)
        sll.add_at_tail(2)
        sll.add_at_tail(3)
        self.assertEqual(str(sll), "1->2->3")

    def test_delete(self):
        sll = SinglyLinkedList()
        sll.add_at_tail(1)
        sll.add_at_tail(2)
        sll.add_at_tail(3)
        sll.delete(2)
        self.assertEqual(str(sll), "1->3")
        sll.delete(1)
        self.assertEqual(str(sll), "3")
        sll.delete(3)
        self.assertEqual(str(sll), "")

    def test_search(self):
        sll = SinglyLinkedList()
        sll.add_at_tail(1)
        sll.add_at_tail(2)
        sll.add_at_tail(3)
        self.assertTrue(sll.search(2))
        self.assertFalse(sll.search(4))

if __name__ == "__main__":
    unittest.main()