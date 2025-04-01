def can_complete_circuit(gas, cost):
    """
    LeetCode Problem 134: Gas Station
    Link: https://leetcode.com/problems/gas-station/

    Problem:
    There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next station.
    Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

    Approach:
    - Calculate the total gas and total cost to determine if a solution is possible.
    - Use a greedy approach to find the starting station by resetting the current tank whenever it becomes negative.

    Args:
        gas (List[int]): Amount of gas at each station.
        cost (List[int]): Cost of gas to travel to the next station.

    Returns:
        int: Starting gas station index, or -1 if not possible.
    """
    total_tank, current_tank = 0, 0  # Total and current gas balance
    start_index = 0  # Starting gas station index

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]  # Update total gas balance
        current_tank += gas[i] - cost[i]  # Update current gas balance

        if current_tank < 0:  # If current tank is negative, reset starting index
            start_index = i + 1
            current_tank = 0

    return start_index if total_tank >= 0 else -1  # Return start index if total gas is sufficient