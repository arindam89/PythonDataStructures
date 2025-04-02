"""
Test cases for the Cheapest Flights Within K Stops problem.

Additional Notes:
- The test cases cover various scenarios, including:
  1. A direct flight with no stops.
  2. A flight with exactly k stops.
  3. A flight with more than k stops.
  4. No valid route exists.
"""

import unittest
from src.leetcode.graph.cheapest_flights_within_k_stops import find_cheapest_price

class TestCheapestFlightsWithinKStops(unittest.TestCase):
    def test_direct_flight(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 0
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 500)

    def test_exactly_k_stops(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        src = 0
        dst = 2
        k = 1
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 200)

    def test_more_than_k_stops(self):
        n = 4
        flights = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [0, 3, 500]]
        src = 0
        dst = 3
        k = 1
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), 500)

    def test_no_valid_route(self):
        n = 3
        flights = [[0, 1, 100], [1, 2, 100]]
        src = 0
        dst = 2
        k = 0
        self.assertEqual(find_cheapest_price(n, flights, src, dst, k), -1)

if __name__ == "__main__":
    unittest.main()