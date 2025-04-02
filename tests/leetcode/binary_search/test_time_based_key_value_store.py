import unittest
from src.leetcode.binary_search.time_based_key_value_store import TimeMap

class TestTimeMap(unittest.TestCase):
    def test_set_and_get(self):
        time_map = TimeMap()
        time_map.set("foo", "bar", 1)
        self.assertEqual(time_map.get("foo", 1), "bar")
        self.assertEqual(time_map.get("foo", 3), "bar")

    def test_overwrite_value(self):
        time_map = TimeMap()
        time_map.set("foo", "bar", 1)
        time_map.set("foo", "bar2", 4)
        self.assertEqual(time_map.get("foo", 4), "bar2")
        self.assertEqual(time_map.get("foo", 5), "bar2")

    def test_no_key(self):
        time_map = TimeMap()
        self.assertEqual(time_map.get("foo", 1), "")

    def test_no_valid_timestamp(self):
        time_map = TimeMap()
        time_map.set("foo", "bar", 10)
        self.assertEqual(time_map.get("foo", 5), "")

if __name__ == "__main__":
    unittest.main()