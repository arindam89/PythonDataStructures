"""
LeetCode Problem: Multiply Strings
Link: https://leetcode.com/problems/multiply-strings/

Problem Statement:
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note:
- The input strings do not contain any leading zeros, except the number "0" itself.
- You must not use any built-in BigInteger library or convert the inputs to integer directly.

Approach:
1. Simulate the multiplication process as done manually.
2. Use an array to store intermediate results for each digit multiplication.
3. Handle carry and convert the result array to a string.

Time Complexity: O(m * n), where m and n are the lengths of num1 and num2.
Space Complexity: O(m + n), for the result array.
"""

def multiply(num1, num2):
    """Multiplies two non-negative integers represented as strings."""
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    result = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            sum = mul + result[i + j + 1]
            result[i + j + 1] = sum % 10
            result[i + j] += sum // 10

    # Convert result array to string, skipping leading zeros
    result_str = "".join(map(str, result)).lstrip("0")
    return result_str if result_str else "0"