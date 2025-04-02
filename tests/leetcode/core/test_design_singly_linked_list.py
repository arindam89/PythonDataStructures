import unittest
from src.leetcode.core.design_singly_linked_list import MyLinkedList

class TestMyLinkedList(unittest.TestCase):
    def test_operations(self):
        linked_list = MyLinkedList()

        # Test addAtHead
        linked_list.addAtHead(1)
        self.assertEqual(linked_list.get(0), 1)

        # Test addAtTail
        linked_list.addAtTail(3)
        self.assertEqual(linked_list.get(1), 3)

        # Test addAtIndex
        linked_list.addAtIndex(1, 2)  # Linked list becomes 1->2->3
        self.assertEqual(linked_list.get(1), 2)

        # Test get
        self.assertEqual(linked_list.get(0), 1)
        self.assertEqual(linked_list.get(1), 2)
        self.assertEqual(linked_list.get(2), 3)
        self.assertEqual(linked_list.get(3), -1)  # Invalid index

        # Test deleteAtIndex
        linked_list.deleteAtIndex(1)  # Linked list becomes 1->3
        self.assertEqual(linked_list.get(1), 3)

        linked_list.deleteAtIndex(0)  # Linked list becomes 3
        self.assertEqual(linked_list.get(0), 3)

        linked_list.deleteAtIndex(0)  # Linked list becomes empty
        self.assertEqual(linked_list.get(0), -1)

if __name__ == "__main__":
    unittest.main()