import unittest
from leetcode.greedy.partition_labels import partition_labels

class TestPartitionLabels(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(partition_labels("ababcbacadefegdehijhklij"), [9,7,8])

    def test_single_partition(self):
        self.assertEqual(partition_labels("aaaaa"), [5])

    def test_multiple_partitions(self):
        self.assertEqual(partition_labels("abac"), [2,2])

if __name__ == "__main__":
    unittest.main()