import unittest
from leetcode.greedy.gas_station import can_complete_circuit

class TestGasStation(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(can_complete_circuit([1,2,3,4,5], [3,4,5,1,2]), 3)

    def test_no_solution(self):
        self.assertEqual(can_complete_circuit([2,3,4], [3,4,3]), -1)

    def test_single_station(self):
        self.assertEqual(can_complete_circuit([1], [1]), 0)

if __name__ == "__main__":
    unittest.main()