import unittest
from leetcode.core.hash_table import HashTable

class TestHashTable(unittest.TestCase):

    def test_put_and_get(self):
        ht = HashTable()
        ht.put(1, 1)
        ht.put(2, 2)
        self.assertEqual(ht.get(1), 1)
        self.assertEqual(ht.get(2), 2)
        self.assertEqual(ht.get(3), -1)

    def test_update_value(self):
        ht = HashTable()
        ht.put(1, 1)
        ht.put(1, 10)
        self.assertEqual(ht.get(1), 10)

    def test_remove(self):
        ht = HashTable()
        ht.put(1, 1)
        ht.put(2, 2)
        ht.remove(1)
        self.assertEqual(ht.get(1), -1)
        self.assertEqual(ht.get(2), 2)

if __name__ == "__main__":
    unittest.main()