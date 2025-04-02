import unittest
from src.leetcode.linked_list.reverse_nodes_in_k_group import ListNode, reverse_k_group

class TestReverseKGroup(unittest.TestCase):
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

    def test_reverse_k_group(self):
        # Test case 1: Normal case with k = 2
        head = self.array_to_list([1, 2, 3, 4, 5])
        new_head = reverse_k_group(head, 2)
        self.assertEqual(self.list_to_array(new_head), [2, 1, 4, 3, 5])

        # Test case 2: Normal case with k = 3
        head = self.array_to_list([1, 2, 3, 4, 5])
        new_head = reverse_k_group(head, 3)
        self.assertEqual(self.list_to_array(new_head), [3, 2, 1, 4, 5])

        # Test case 3: k larger than list length
        head = self.array_to_list([1, 2])
        new_head = reverse_k_group(head, 3)
        self.assertEqual(self.list_to_array(new_head), [1, 2])

if __name__ == "__main__":
    unittest.main()