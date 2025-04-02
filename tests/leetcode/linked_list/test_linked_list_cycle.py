import unittest
from src.leetcode.linked_list.linked_list_cycle import ListNode, has_cycle

class TestLinkedListCycle(unittest.TestCase):
    def test_has_cycle(self):
        # Test case 1: List with a cycle
        head = ListNode(3)
        second = ListNode(2)
        third = ListNode(0)
        fourth = ListNode(-4)
        head.next = second
        second.next = third
        third.next = fourth
        fourth.next = second  # Creates a cycle
        self.assertTrue(has_cycle(head))

        # Test case 2: List without a cycle
        head = ListNode(1)
        second = ListNode(2)
        head.next = second
        self.assertFalse(has_cycle(head))

        # Test case 3: Single node without a cycle
        head = ListNode(1)
        self.assertFalse(has_cycle(head))

        # Test case 4: Empty list
        head = None
        self.assertFalse(has_cycle(head))

if __name__ == "__main__":
    unittest.main()