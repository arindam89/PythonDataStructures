import unittest
from src.leetcode.linked_list.merge_two_sorted_lists import ListNode, merge_two_sorted_lists

class TestMergeTwoSortedLists(unittest.TestCase):
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

    def test_merge_two_sorted_lists(self):
        # Test case 1: Normal case
        list1 = self.array_to_list([1, 2, 4])
        list2 = self.array_to_list([1, 3, 4])
        merged_head = merge_two_sorted_lists(list1, list2)
        self.assertEqual(self.list_to_array(merged_head), [1, 1, 2, 3, 4, 4])

        # Test case 2: One list is empty
        list1 = self.array_to_list([])
        list2 = self.array_to_list([0])
        merged_head = merge_two_sorted_lists(list1, list2)
        self.assertEqual(self.list_to_array(merged_head), [0])

        # Test case 3: Both lists are empty
        list1 = self.array_to_list([])
        list2 = self.array_to_list([])
        merged_head = merge_two_sorted_lists(list1, list2)
        self.assertEqual(self.list_to_array(merged_head), [])

if __name__ == "__main__":
    unittest.main()