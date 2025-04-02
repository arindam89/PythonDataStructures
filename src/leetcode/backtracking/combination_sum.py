# LeetCode 39: Combination Sum
# https://leetcode.com/problems/combination-sum/
#
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
#
# Approach:
# - Use backtracking to explore all possible combinations.
# - At each step, decide whether to include the current candidate in the combination.
# - If the sum of the current combination equals the target, add it to the result.
# - If the sum exceeds the target, backtrack.

def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            # Found a valid combination
            result.append(path[:])
            return
        if target < 0:
            # Exceeded the target, stop exploring
            return
        for i in range(start, len(candidates)):
            # Include candidates[i] in the combination
            path.append(candidates[i])
            # Recurse with the updated target
            backtrack(i, target - candidates[i], path)
            # Backtrack by removing candidates[i]
            path.pop()

    result = []
    backtrack(0, target, [])
    return result