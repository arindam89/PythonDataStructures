import unittest
from leetcode.core.dynamic_array import DynamicArray

class TestDynamicArray(unittest.TestCase):
    def test_append(self):
        dynamic_array = DynamicArray()
        dynamic_array.append(1)
        dynamic_array.append(2)
        self.assertEqual(len(dynamic_array), 2)
        self.assertEqual(str(dynamic_array), "[1, 2]")

    def test_get(self):
        dynamic_array = DynamicArray()
        dynamic_array.append(1)
        dynamic_array.append(2)
        self.assertEqual(dynamic_array.get(0), 1)
        self.assertEqual(dynamic_array.get(1), 2)
        with self.assertRaises(IndexError):
            dynamic_array.get(2)

    def test_remove(self):
        dynamic_array = DynamicArray()
        dynamic_array.append(1)
        dynamic_array.append(2)
        dynamic_array.append(3)
        dynamic_array.remove(1)
        self.assertEqual(len(dynamic_array), 2)
        self.assertEqual(str(dynamic_array), "[1, 3]")
        with self.assertRaises(IndexError):
            dynamic_array.remove(2)

    def test_resize(self):
        dynamic_array = DynamicArray()
        for i in range(100):
            dynamic_array.append(i)
        self.assertEqual(len(dynamic_array), 100)
        for i in range(100):
            self.assertEqual(dynamic_array.get(i), i)

if __name__ == "__main__":
    unittest.main()