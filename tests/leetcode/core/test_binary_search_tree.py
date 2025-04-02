import unittest
from leetcode.core.binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def test_insert_and_inorder(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(2)
        bst.insert(4)
        bst.insert(6)
        bst.insert(8)
        self.assertEqual(bst.inorder(), [2, 3, 4, 5, 6, 7, 8])

    def test_search(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        self.assertTrue(bst.search(5))
        self.assertTrue(bst.search(3))
        self.assertFalse(bst.search(10))

    def test_delete(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(2)
        bst.insert(4)
        bst.delete(3)
        self.assertEqual(bst.inorder(), [2, 4, 5, 7])
        bst.delete(5)
        self.assertEqual(bst.inorder(), [2, 4, 7])

if __name__ == "__main__":
    unittest.main()