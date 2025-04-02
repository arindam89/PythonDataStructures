import unittest
from src.leetcode.linked_list.lru_cache import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_lru_cache(self):
        # Test case 1: Basic operations
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 1)  # Returns 1
        lru.put(3, 3)  # Evicts key 2
        self.assertEqual(lru.get(2), -1)  # Returns -1 (not found)
        lru.put(4, 4)  # Evicts key 1
        self.assertEqual(lru.get(1), -1)  # Returns -1 (not found)
        self.assertEqual(lru.get(3), 3)  # Returns 3
        self.assertEqual(lru.get(4), 4)  # Returns 4

        # Test case 2: Overwriting existing key
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(1, 10)  # Overwrite key 1
        self.assertEqual(lru.get(1), 10)  # Returns 10

        # Test case 3: Capacity of 1
        lru = LRUCache(1)
        lru.put(1, 1)
        lru.put(2, 2)  # Evicts key 1
        self.assertEqual(lru.get(1), -1)  # Returns -1 (not found)
        self.assertEqual(lru.get(2), 2)  # Returns 2

if __name__ == "__main__":
    unittest.main()