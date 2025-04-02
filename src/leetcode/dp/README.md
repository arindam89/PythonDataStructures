# Dynamic Programming (DP) Solutions

This folder contains Python implementations of various dynamic programming problems. Each solution is accompanied by detailed explanations and comments to help understand the approach and logic used.

## Problems and Solutions

### 1. Climbing Stairs
- **Description**: Given `n` stairs, you can climb 1 or 2 steps at a time. Find the number of distinct ways to reach the top.
- **Complexity**: 
  - Time: O(n)
  - Space: O(1)

### 2. Coin Change
- **Description**: Given an array of coins and a target amount, find the minimum number of coins needed to make the amount.
- **Complexity**: 
  - Time: O(amount * len(coins))
  - Space: O(amount)

### 3. Decode Ways
- **Description**: Given a string of digits, determine the number of ways to decode it into letters (A=1, B=2, ..., Z=26).
- **Complexity**: 
  - Time: O(n)
  - Space: O(n)

### 4. House Robber
- **Description**: Given an array of non-negative integers representing the amount of money in each house, determine the maximum amount you can rob without robbing adjacent houses.
- **Complexity**: 
  - Time: O(n)
  - Space: O(1)

### 5. House Robber II
- **Description**: Similar to House Robber, but houses are arranged in a circle.
- **Complexity**: 
  - Time: O(n)
  - Space: O(1)

### 6. Longest Common Subsequence
- **Description**: Given two strings, find the length of their longest common subsequence.
- **Complexity**: 
  - Time: O(m * n)
  - Space: O(m * n)

### 7. Longest Increasing Subsequence
- **Description**: Find the length of the longest strictly increasing subsequence in an array.
- **Complexity**: 
  - Time: O(n^2) or O(n log n) (with binary search)
  - Space: O(n)

### 8. Longest Palindromic Substring
- **Description**: Find the longest substring in a string that is a palindrome.
- **Complexity**: 
  - Time: O(n^2)
  - Space: O(n^2)

### 9. Maximum Product Subarray
- **Description**: Find the contiguous subarray within an array that has the largest product.
- **Complexity**: 
  - Time: O(n)
  - Space: O(1)

### 10. Min Cost Climbing Stairs
- **Description**: Given an array of costs, find the minimum cost to reach the top of the stairs.
- **Complexity**: 
  - Time: O(n)
  - Space: O(1)

### 11. Palindromic Substrings
- **Description**: Count the number of palindromic substrings in a string.
- **Complexity**: 
  - Time: O(n^2)
  - Space: O(1)

### 12. Partition Equal Subset Sum
- **Description**: Determine if an array can be partitioned into two subsets with equal sums.
- **Complexity**: 
  - Time: O(n * sum/2)
  - Space: O(sum/2)

### 13. Word Break
- **Description**: Given a string and a dictionary of words, determine if the string can be segmented into a space-separated sequence of dictionary words.
- **Complexity**: 
  - Time: O(n^2)
  - Space: O(n)

## Solution Explanations

Each problem in this folder is solved using dynamic programming techniques. Below is a brief explanation of the approach used for each problem:

### 1. Climbing Stairs
- **Approach**: Use a bottom-up DP approach where the number of ways to reach the `i-th` step is the sum of ways to reach `(i-1)-th` and `(i-2)-th` steps.

### 2. Coin Change
- **Approach**: Use a DP array where each index represents the minimum coins needed to make that amount. Update the array iteratively for each coin.

### 3. Decode Ways
- **Approach**: Use a DP array where each index represents the number of ways to decode the string up to that point. Handle single and double-digit decodings.

### 4. House Robber
- **Approach**: Use two variables to keep track of the maximum amount robbed up to the previous house and the house before that.

### 5. House Robber II
- **Approach**: Solve the problem twice: once excluding the first house and once excluding the last house, then take the maximum of the two results.

### 6. Longest Common Subsequence
- **Approach**: Use a 2D DP table where each cell represents the length of the LCS for substrings up to those indices.

### 7. Longest Increasing Subsequence
- **Approach**: Use a DP array where each index represents the length of the LIS ending at that index. Optionally, use binary search for optimization.

### 8. Longest Palindromic Substring
- **Approach**: Use a 2D DP table where each cell represents whether a substring is a palindrome. Expand around centers for optimization.

### 9. Maximum Product Subarray
- **Approach**: Use two variables to keep track of the maximum and minimum product up to the current index, as the minimum can become maximum when multiplied by a negative number.

### 10. Min Cost Climbing Stairs
- **Approach**: Use a bottom-up DP approach where the cost to reach the `i-th` step is the minimum of the costs to reach `(i-1)-th` and `(i-2)-th` steps plus the cost of the current step.

### 11. Palindromic Substrings
- **Approach**: Use a 2D DP table or expand around centers to count all palindromic substrings in the string.

### 12. Partition Equal Subset Sum
- **Approach**: Use a DP array where each index represents whether a subset with that sum is possible. Update the array iteratively for each number.

### 13. Word Break
- **Approach**: Use a DP array where each index represents whether the substring up to that index can be segmented into dictionary words. Check all possible splits iteratively.

## Important Notes
1. **Understand the State Transition**: The key to solving DP problems is identifying the state and the transition between states.
2. **Optimize Space**: Many DP problems can be optimized from O(n) space to O(1) space by reusing variables.
3. **Practice**: The more problems you solve, the better you will understand patterns in DP.

Feel free to explore the solutions and test cases to deepen your understanding of dynamic programming.