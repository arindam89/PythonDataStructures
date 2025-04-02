import unittest
from src.leetcode.linked_list.remove_nth_node_from_end import ListNode, remove_nth_from_end

class TestRemoveNthFromEnd(unittest.TestCase):
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

    def test_remove_nth_from_end(self):
        # Test case 1: Remove 2nd node from end
        head = self.array_to_list([1, 2, 3, 4, 5])
        new_head = remove_nth_from_end(head, 2)
        self.assertEqual(self.list_to_array(new_head), [1, 2, 3, 5])

        # Test case 2: Remove the only node
        head = self.array_to_list([1])
        new_head = remove_nth_from_end(head, 1)
        self.assertEqual(self.list_to_array(new_head), [])

        # Test case 3: Remove the head node
        head = self.array_to_list([1, 2])
        new_head = remove_nth_from_end(head, 2)
        self.assertEqual(self.list_to_array(new_head), [2])

if __name__ == "__main__":
    unittest.main()