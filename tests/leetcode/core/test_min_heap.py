import unittest
from leetcode.core.min_heap import MinHeap

class TestMinHeap(unittest.TestCase):

    def test_insert_and_extract_min(self):
        heap = MinHeap()
        heap.insert(3)
        heap.insert(1)
        heap.insert(2)
        self.assertEqual(heap.extract_min(), 1)
        self.assertEqual(heap.extract_min(), 2)
        self.assertEqual(heap.extract_min(), 3)

    def test_delete(self):
        heap = MinHeap()
        heap.insert(3)
        heap.insert(1)
        heap.insert(2)
        heap.delete(2)
        self.assertEqual(str(heap), "[1, 3]")
        with self.assertRaises(ValueError):
            heap.delete(4)

    def test_empty_extract(self):
        heap = MinHeap()
        with self.assertRaises(IndexError):
            heap.extract_min()

if __name__ == "__main__":
    unittest.main()