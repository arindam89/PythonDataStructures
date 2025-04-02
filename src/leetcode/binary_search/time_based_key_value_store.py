# Problem: Time Based Key-Value Store
# Link: https://leetcode.com/problems/time-based-key-value-store/
# Difficulty: Medium
#
# Approach:
# - Use a dictionary to store keys and their corresponding list of (timestamp, value) pairs.
# - For `set` operation, append the (timestamp, value) pair to the list for the key.
# - For `get` operation, use binary search to find the largest timestamp less than or equal to the given timestamp.
#
# Time Complexity:
# - `set`: O(1) for appending to the list.
# - `get`: O(log n) for binary search, where n is the number of timestamps for the key.
# Space Complexity: O(n), where n is the total number of (timestamp, value) pairs stored.

from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        """
        Initialize the data structure.
        """
        self.store = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        Store the key-value pair along with the timestamp.

        :param key: str - The key.
        :param value: str - The value.
        :param timestamp: int - The timestamp.
        """
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        Retrieve the value for the key with the largest timestamp <= given timestamp.

        :param key: str - The key.
        :param timestamp: int - The timestamp.
        :return: str - The value, or "" if no such timestamp exists.
        """
        if key not in self.store:
            return ""

        values = self.store[key]
        i = bisect.bisect_right(values, (timestamp, chr(127)))  # chr(127) is a high ASCII character
        return values[i - 1][1] if i > 0 else ""