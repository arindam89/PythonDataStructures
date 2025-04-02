import unittest
from src.leetcode.linked_list.copy_list_with_random_pointer import Node, copy_random_list

class TestCopyRandomList(unittest.TestCase):
    def list_to_array(self, head):
        """Helper function to convert linked list to array for easy comparison."""
        array = []
        while head:
            array.append((head.val, head.random.val if head.random else None))
            head = head.next
        return array

    def array_to_list(self, array):
        """Helper function to convert array to linked list with random pointers."""
        if not array:
            return None
        nodes = [Node(val) for val, _ in array]
        for i, (_, random_index) in enumerate(array):
            if i < len(array) - 1:
                nodes[i].next = nodes[i + 1]
            if random_index is not None:
                nodes[i].random = nodes[random_index]
        return nodes[0]

    def test_copy_random_list(self):
        # Test case 1: Normal case with random pointers
        head = self.array_to_list([(7, None), (13, 0), (11, 4), (10, 2), (1, 0)])
        copied_head = copy_random_list(head)
        self.assertEqual(self.list_to_array(copied_head), [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)])

        # Test case 2: Single node with no random pointer
        head = self.array_to_list([(1, None)])
        copied_head = copy_random_list(head)
        self.assertEqual(self.list_to_array(copied_head), [(1, None)])

        # Test case 3: Empty list
        head = self.array_to_list([])
        copied_head = copy_random_list(head)
        self.assertEqual(self.list_to_array(copied_head), [])

if __name__ == "__main__":
    unittest.main()