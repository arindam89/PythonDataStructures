import unittest
from src.leetcode.linked_list.merge_k_sorted_lists import ListNode, merge_k_sorted_lists

class TestMergeKSortedLists(unittest.TestCase):
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

    def test_merge_k_sorted_lists(self):
        # Test case 1: Normal case with multiple lists
        lists = [
            self.array_to_list([1, 4, 5]),
            self.array_to_list([1, 3, 4]),
            self.array_to_list([2, 6])
        ]
        merged_head = merge_k_sorted_lists(lists)
        self.assertEqual(self.list_to_array(merged_head), [1, 1, 2, 3, 4, 4, 5, 6])

        # Test case 2: Empty lists
        lists = [
            self.array_to_list([]),
            self.array_to_list([]),
            self.array_to_list([])
        ]
        merged_head = merge_k_sorted_lists(lists)
        self.assertEqual(self.list_to_array(merged_head), [])

        # Test case 3: Single list
        lists = [
            self.array_to_list([1, 2, 3])
        ]
        merged_head = merge_k_sorted_lists(lists)
        self.assertEqual(self.list_to_array(merged_head), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()