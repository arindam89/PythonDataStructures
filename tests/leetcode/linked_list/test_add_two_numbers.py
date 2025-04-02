import unittest
from src.leetcode.linked_list.add_two_numbers import ListNode, add_two_numbers

class TestAddTwoNumbers(unittest.TestCase):
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

    def test_add_two_numbers(self):
        # Test case 1: Normal case
        l1 = self.array_to_list([2, 4, 3])
        l2 = self.array_to_list([5, 6, 4])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.list_to_array(result), [7, 0, 8])

        # Test case 2: Different lengths
        l1 = self.array_to_list([1, 8])
        l2 = self.array_to_list([0])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.list_to_array(result), [1, 8])

        # Test case 3: With carry
        l1 = self.array_to_list([9, 9, 9])
        l2 = self.array_to_list([1])
        result = add_two_numbers(l1, l2)
        self.assertEqual(self.list_to_array(result), [0, 0, 0, 1])

if __name__ == "__main__":
    unittest.main()