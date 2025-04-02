"""
LeetCode Problem: Maximum Product Subarray
Link: https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

Approach:
We use a dynamic programming approach to solve this problem. At each index, we keep track of the maximum and minimum product ending at that index.
1. The maximum product at index i is the maximum of:
   - nums[i]
   - nums[i] * max_product[i-1]
   - nums[i] * min_product[i-1]
2. Similarly, the minimum product at index i is the minimum of the above three values.
3. The result is the maximum value of max_product across all indices.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_product(nums: list[int]) -> int:
    if not nums:
        return 0

    max_product = min_product = result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], nums[i] * max_product)
        min_product = min(nums[i], nums[i] * min_product)

        result = max(result, max_product)

    return result