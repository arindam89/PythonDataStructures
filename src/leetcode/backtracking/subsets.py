# LeetCode 78: Subsets
# https://leetcode.com/problems/subsets/
#
# Given an integer array nums of unique elements, return all possible subsets (the power set).
#
# Approach:
# - Use backtracking to explore all possible subsets.
# - At each step, decide whether to include the current element in the subset or not.
# - Add the current subset to the result list.

def subsets(nums):
    def backtrack(start, path):
        # Add the current subset to the result
        result.append(path[:])
        for i in range(start, len(nums)):
            # Include nums[i] in the subset
            path.append(nums[i])
            # Recurse with the next starting index
            backtrack(i + 1, path)
            # Backtrack by removing nums[i]
            path.pop()

    result = []
    backtrack(0, [])
    return result