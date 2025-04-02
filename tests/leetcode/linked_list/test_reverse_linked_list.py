import unittest
from src.leetcode.linked_list.reverse_linked_list import ListNode, reverse_linked_list

class TestReverseLinkedList(unittest.TestCase):
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

    def test_reverse_linked_list(self):
        # Test case 1: Normal case
        head = self.array_to_list([1, 2, 3, 4, 5])
        reversed_head = reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [5, 4, 3, 2, 1])

        # Test case 2: Single element
        head = self.array_to_list([1])
        reversed_head = reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [1])

        # Test case 3: Empty list
        head = self.array_to_list([])
        reversed_head = reverse_linked_list(head)
        self.assertEqual(self.list_to_array(reversed_head), [])

if __name__ == "__main__":
    unittest.main()