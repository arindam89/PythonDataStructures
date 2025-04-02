import unittest
from datastructures.core.dynamic_array import DynamicArray

class TestDynamicArray(unittest.TestCase):

    def test_append(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)
        self.assertEqual(len(arr), 3)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 3)

    def test_insert(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(3)
        arr.insert(1, 2)
        self.assertEqual(len(arr), 3)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 3)

    def test_delete(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)
        arr.delete(1)
        self.assertEqual(len(arr), 2)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 3)

    def test_resize(self):
        arr = DynamicArray()
        for i in range(100):
            arr.append(i)
        self.assertEqual(len(arr), 100)
        for i in range(100):
            self.assertEqual(arr[i], i)

    def test_out_of_bounds(self):
        arr = DynamicArray()
        with self.assertRaises(IndexError):
            _ = arr[0]
        arr.append(1)
        with self.assertRaises(IndexError):
            _ = arr[2]

if __name__ == "__main__":
    unittest.main()