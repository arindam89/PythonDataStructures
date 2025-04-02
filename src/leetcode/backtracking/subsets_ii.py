# LeetCode 90: Subsets II
# https://leetcode.com/problems/subsets-ii/
#
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets.
#
# Approach:
# - Use backtracking to explore all possible subsets.
# - Sort the array to handle duplicates easily.
# - At each step, decide whether to include the current element in the subset or not.
# - Skip duplicate elements to ensure unique subsets.

def subsets_with_dup(nums):
    def backtrack(start, path):
        # Add the current subset to the result
        result.append(path[:])
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            # Include nums[i] in the subset
            path.append(nums[i])
            # Recurse with the next starting index
            backtrack(i + 1, path)
            # Backtrack by removing nums[i]
            path.pop()

    nums.sort()
    result = []
    backtrack(0, [])
    return result