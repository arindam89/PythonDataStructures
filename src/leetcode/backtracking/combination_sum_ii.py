# LeetCode 40: Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/
#
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
#
# Approach:
# - Use backtracking to explore all possible combinations.
# - Sort the candidates to handle duplicates easily.
# - At each step, decide whether to include the current candidate in the combination.
# - Skip duplicate candidates to ensure unique combinations.

def combination_sum_ii(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            # Found a valid combination
            result.append(path[:])
            return
        if target < 0:
            # Exceeded the target, stop exploring
            return
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            # Include candidates[i] in the combination
            path.append(candidates[i])
            # Recurse with the next starting index
            backtrack(i + 1, target - candidates[i], path)
            # Backtrack by removing candidates[i]
            path.pop()

    candidates.sort()
    result = []
    backtrack(0, target, [])
    return result