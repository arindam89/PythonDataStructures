import unittest
from leetcode.core.disjoint_set import DisjointSet

class TestDisjointSet(unittest.TestCase):

    def test_union_and_find(self):
        ds = DisjointSet(5)
        ds.union(0, 1)
        ds.union(1, 2)
        self.assertTrue(ds.connected(0, 2))
        self.assertFalse(ds.connected(0, 3))

    def test_path_compression(self):
        ds = DisjointSet(5)
        ds.union(0, 1)
        ds.union(1, 2)
        ds.find(2)  # Trigger path compression
        self.assertEqual(ds.parent[2], ds.find(0))

    def test_rank(self):
        ds = DisjointSet(5)
        ds.union(0, 1)
        ds.union(2, 3)
        ds.union(1, 3)
        self.assertTrue(ds.connected(0, 3))

if __name__ == "__main__":
    unittest.main()