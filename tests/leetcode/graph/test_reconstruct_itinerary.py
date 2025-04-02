"""
Test cases for the Reconstruct Itinerary problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A simple itinerary with no branching.
  2. An itinerary with multiple valid paths.
  3. An itinerary with a cycle.
  4. An itinerary starting and ending at the same airport.
"""

import unittest
from src.leetcode.graph.reconstruct_itinerary import find_itinerary

class TestReconstructItinerary(unittest.TestCase):
    def test_simple_itinerary(self):
        tickets = [["JFK", "SFO"], ["SFO", "LAX"]]
        expected = ["JFK", "SFO", "LAX"]
        self.assertEqual(find_itinerary(tickets), expected)

    def test_multiple_valid_paths(self):
        tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
        expected = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
        self.assertEqual(find_itinerary(tickets), expected)

    def test_cycle_in_itinerary(self):
        tickets = [["JFK", "SFO"], ["SFO", "JFK"]]
        expected = ["JFK", "SFO", "JFK"]
        self.assertEqual(find_itinerary(tickets), expected)

    def test_start_and_end_same_airport(self):
        tickets = [["JFK", "ATL"], ["ATL", "JFK"]]
        expected = ["JFK", "ATL", "JFK"]
        self.assertEqual(find_itinerary(tickets), expected)

if __name__ == "__main__":
    unittest.main()