import unittest
from src.leetcode.linked_list.reorder_list import ListNode, reorder_list

class TestReorderList(unittest.TestCase):
    def list_to_array(self, head):
        """Helper function to convert linked list to array for easy comparison."""
        array = []
        while head:
            array.append(head.val)
            head = head.next
        return array

    def array_to_list(self, array):
        """Helper function to convert array to linked list."""
        if not array:
            return None
        head = ListNode(array[0])
        current = head
        for val in array[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def test_reorder_list(self):
        # Test case 1: Normal case
        head = self.array_to_list([1, 2, 3, 4])
        reorder_list(head)
        self.assertEqual(self.list_to_array(head), [1, 4, 2, 3])

        # Test case 2: Single element
        head = self.array_to_list([1])
        reorder_list(head)
        self.assertEqual(self.list_to_array(head), [1])

        # Test case 3: Empty list
        head = self.array_to_list([])
        reorder_list(head)
        self.assertEqual(self.list_to_array(head), [])

if __name__ == "__main__":
    unittest.main()